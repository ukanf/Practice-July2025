import asyncio
import uuid
from db import save_execution, load_execution
from workflow_steps import WORKFLOWS

class DurableEngine:
    _db_lock = asyncio.Lock()  # Class-level lock for DB operations

    def __init__(self):
        pass

    def start_workflow(self, workflow_name):
        execution_id = str(uuid.uuid4())
        execution = {
            "id": execution_id,
            "workflow": workflow_name,
            "state": "running",
            "current_step": None,
            "step_output": {},
        }
        # Synchronous, so no lock needed here
        save_execution(execution)
        return execution_id

    async def run_step_in_thread(self, step_func, execution_id, step_name, context):
        # Lock DB access to avoid race conditions
        async with self._db_lock:
            execution = load_execution(execution_id)
            if execution is None:
                print(f"Execution {execution_id} not found for step {step_name}.")
                return
            context = execution["step_output"]
        print(f"Running {step_name} in thread for execution {execution_id}")
        output = await step_func(context)
        context.update(output)
        async with self._db_lock:
            execution = load_execution(execution_id)
            if execution is None:
                print(f"Execution {execution_id} not found for step {step_name} after step_func.")
                return
            execution["step_output"] = context
            save_execution(execution)
        print(execution)
        print(f"Step {step_name} completed and saved for execution {execution_id}")

    async def resume(self, execution_id):
        async with self._db_lock:
            execution = load_execution(execution_id)
        if not execution or execution["state"] != "running":
            print("Nothing to resume.")
            return

        steps = WORKFLOWS[execution["workflow"]]
        current_index = 0

        if execution["current_step"]:
            step_names = [name for name, *_ in steps]
            if execution["current_step"] in step_names:
                current_index = step_names.index(execution["current_step"]) + 1

        context = execution["step_output"]
        running_tasks = []

        for i in range(current_index, len(steps)):
            step_name, step_func, step_dependencies = steps[i]

            if len(step_dependencies) == 0:
                # create new thread for no dependencies, do not wait for completion
                print(f"Executing {step_name} with no dependencies in a new thread (fire and forget).")
                task = asyncio.create_task(self.run_step_in_thread(step_func, execution_id, step_name, context.copy()))
                running_tasks.append(task)
                continue
            else:
                # Wait for all running tasks to complete before checking dependencies
                if running_tasks:
                    print("Waiting for all async tasks to complete before checking dependencies...")
                    await asyncio.gather(*running_tasks)
                    running_tasks = []
                    # Reload execution to get updated step_output
                    async with self._db_lock:
                        execution = load_execution(execution_id)
                        context = execution["step_output"]

                unmet_deps = [dep for dep in step_dependencies if dep not in execution["step_output"].keys()]
                if unmet_deps:
                    print(f"Skipping {step_name} due to unmet dependencies: {unmet_deps}")
                    continue

            execution["current_step"] = step_name
            async with self._db_lock:
                save_execution(execution)

            print(f"Running {step_name} for execution {execution_id}")
            output = await step_func(context)
            context.update(output)
            async with self._db_lock:
                execution = load_execution(execution_id)
                execution["step_output"] = context
                save_execution(execution)

        # Wait for any remaining async tasks before marking as completed
        if running_tasks:
            print("Waiting for remaining async tasks to complete before finishing execution...")
            await asyncio.gather(*running_tasks)

        execution["state"] = "completed"
        async with self._db_lock:
            save_execution(execution)
        print(f"Execution {execution_id} completed.")
