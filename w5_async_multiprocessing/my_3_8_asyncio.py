# *****************************
#          ASYNCIO
#
# а вот так уже норм PEP 492
# https://docs.python.org/3.6/library/asyncio.html
# *****************************
import asyncio


async def hello_world():
    n = 0
    while True:
        print(f"Hello {n} world!")
        await asyncio.sleep(1.0)
        n += 1


loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
