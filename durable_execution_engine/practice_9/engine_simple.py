import uuid
from db import save_execution, load_execution
from workflow_steps import WORKFLOWS

class SimpleDurableEngine:
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
            "engine_type": "",  # This will be set only when the workflow is completed
            "execution_time": 0.0 # This will be set only when the workflow is completed
        }
        save_execution(execution)
        return execution_id

    async def resume(self, execution_id):
        execution = load_execution(execution_id)
        if not execution or execution["state"] != "running":
            print("Nothing to resume.")
            return

        steps = WORKFLOWS[execution["workflow"]]
        current_index = 0

        if execution["current_step"]:
            step_id = [id for id, _, _ in steps]
            print(step_id)
            if execution["current_step"] in step_id:
                current_index = step_id.index(execution["current_step"])

        context = execution["step_output"]

        for i in range(current_index, len(steps)):
            step_name, step_func, _ = steps[i]
            execution["current_step"] = step_name
            save_execution(execution)

            print(f"Running ID: {step_name} for execution {execution_id}")
            output = await step_func(context) # output = "step_name"
            if output in context.keys():
                context[output] += 1
            else:
                context[output] = 1
            execution["step_output"] = context
            save_execution(execution)

        execution["state"] = "completed"
        save_execution(execution)
        print(f"Execution {execution_id} completed.")