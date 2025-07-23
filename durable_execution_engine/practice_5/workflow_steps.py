import asyncio
import time

async def step_1(context=None):
    print("Executing step 1")
    await asyncio.sleep(1)
    # time.sleep(1)
    return {"step_1": "done"}

async def step_2(context=None):
    print("Executing step 2")
    await asyncio.sleep(1)
    # time.sleep(1)
    return {"step_2": "done"}

async def step_3(context=None):
    print("Executing step 3")
    await asyncio.sleep(1)
    # time.sleep(1)
    return {"step_3": "done"}

async def no_dep_step(context=None):
    print("Executing no_dep_step")
    await asyncio.sleep(1)
    # time.sleep(1)
    return {"no_dep_step": "done"}

WORKFLOWS = {
    "supported_workflow": [
        ("step_1", step_1, []),
        ("step_2", step_2, ["step_1"]),
        ("no_dep_step", no_dep_step, []),
        ("no_dep_step", no_dep_step, []),
        ("step_3", step_3, ["step_2"]),
        ("no_dep_step", no_dep_step, []),
        ("no_dep_step", no_dep_step, []),
        ("step_2", step_2, ["step_1"]),
    ],
    "harder_async_workflow": [
        ("step_1", step_1, []),
        ("no_dep_step", no_dep_step, []),
        ("step_2", step_2, ["step_1"]),
        ("no_dep_step", no_dep_step, []),
        ("no_dep_step", no_dep_step, []),
        ("step_3", step_3, ["step_2"]),
        ("no_dep_step", no_dep_step, []),
        ("no_dep_step", no_dep_step, []),
        ("step_2", step_2, ["step_1"]),
    ]
}
