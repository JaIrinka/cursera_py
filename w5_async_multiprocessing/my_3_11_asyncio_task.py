# *****************************
#        ASYNCIO. TASK
# *****************************
import asyncio


async def sleep_task(num):
    for i in range(5):
        print(f"process task: {num}; iter: {i}")
        await asyncio.sleep(1)

    return num


loop = asyncio.get_event_loop()
task_list = [loop.create_task(sleep_task(i)) for i in range(2)]

r1 = loop.run_until_complete(asyncio.wait(task_list))
print(r1)
print("---------------------")

r2 = loop.run_until_complete(loop.create_task(sleep_task(3)))
print(r2)
print("---------------------")

r3 = loop.run_until_complete(asyncio.gather(sleep_task(10), sleep_task(20),))
print(r3)
