import asyncio
import time

async def step_1(context=None):
    print("Executing step 1")
    await asyncio.sleep(1)
    # time.sleep(1)
    return "step_1"

async def step_2(context=None):
    print("Executing step 2")
    await asyncio.sleep(1)
    # time.sleep(1)
    return "step_2"

async def step_3(context=None):
    print("Executing step 3")
    await asyncio.sleep(1)
    # time.sleep(1)
    return "step_3"

async def no_dep_step(context=None):
    print("Executing no_dep_step")
    await asyncio.sleep(1)
    # time.sleep(1)
    return "no_dep_step"

WORKFLOWS = {
    "workflows_1": [
        ("step_1", step_1, []),
        ("step_2", step_2, ["step_1"]),
        ("no_dep_step", no_dep_step, []),
        ("step_3", step_3, ["step_2"]),
        ("no_dep_step", no_dep_step, []),
        ("step_2", step_2, ["step_1"]),
    ]
}
