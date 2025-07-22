import asyncio
from db import init_db
from engine import DurableEngine

async def main():
    init_db()
    engine = DurableEngine()

    # Start new workflow
    execution_id = engine.start_workflow("example_workflow")
    print(f"Started workflow: {execution_id}")

    # Resume (or run) workflow
    await engine.resume(execution_id)

if __name__ == "__main__":
    asyncio.run(main())
