# *****************************
#          ASYNCIO
#
# устаревший вариант! Будет предупреждение depricated - это значит, нужно использовать кое-что поновее
# *****************************
import asyncio


@asyncio.coroutines.coroutine
def hello_world_old():
    n = 0
    while True:
        if n > 10:
            break
        print(f"Hello OLD {n} world!")
        yield from asyncio.sleep(2)
        n += 1


loop_old = asyncio.get_event_loop()
loop_old.run_until_complete(hello_world_old())
loop_old.close()
