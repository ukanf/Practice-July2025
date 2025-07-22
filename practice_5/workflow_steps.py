import asyncio

async def step_1(context):
    print("Executing step 1")
    await asyncio.sleep(1)
    return {"step1": "done"}

async def step_2(context):
    print("Executing step 2")
    await asyncio.sleep(1)
    return {"step2": "done"}

async def step_3(context):
    print("Executing step 3")
    await asyncio.sleep(1)
    return {"step3": "done"}

async def my_step_4(context):
    print("Executing my_step_4")
    await asyncio.sleep(1)
    return {"my_step_4": "done"}

WORKFLOWS = {
    "example_workflow": [
        ("step_1", step_1),
        ("step_2", step_2),
        ("step_3", step_3),
        ("my_step_4", my_step_4),
    ]
}
