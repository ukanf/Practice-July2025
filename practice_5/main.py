import asyncio
import time
from db import init_db
from engine_async import AsyncDurableEngine
from engine_simple import SimpleDurableEngine


async def main():
    start_time = time.time()
    init_db()
    engine_kind = "async"  # or "simple" for the synchronous version
    if engine_kind == "async":
        engine = AsyncDurableEngine()
    elif engine_kind == "simple":
        engine = SimpleDurableEngine()
    else:
        raise ValueError("Unknown engine kind specified. Use 'async' or 'simple'.")

    # Start new workflow
    execution_id = engine.start_workflow("harder_async_workflow")
    print(f"Started workflow: {execution_id}")

    # Resume (or run) workflow
    await engine.resume(execution_id)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
