import asyncio
import time
from db import init_db
from engine_async import AsyncDurableEngine
from engine_simple import SimpleDurableEngine
from db import save_execution, load_execution

async def main():
    start_time = time.time()
    init_db()
    engine_kind = "simple"
    if engine_kind == "async":
        engine = AsyncDurableEngine()
    elif engine_kind == "simple":
        engine = SimpleDurableEngine()
    else:
        raise ValueError("Unknown engine kind specified. Use 'async' or 'simple'.")

    # Start new workflow
    execution_id = engine.start_workflow("harder_async_workflow")
    print(f"Started workflow: {execution_id}")
    
    # Run the workflow
    await engine.resume(execution_id)

    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")

    # Load the execution to save the execution time and engine type
    execution = load_execution(execution_id)
    # Save execution time and engine type
    execution["execution_time"] = f"{execution_time:.4f}"
    execution["engine_type"] = engine_kind
    save_execution(execution)
    # TODO: there is a problem when resuming a workflow because the time won't be true... we have to deal with it differently - maybe "if resume then don't save execution time"... well, we need that flag to know if resume and it really just depends on the input and who is changing this.. doesnt matter right now.

if __name__ == "__main__":
    asyncio.run(main())
