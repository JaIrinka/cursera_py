# *****************************
#      ASYNCIO. EXECUTER
# *****************************
import asyncio
from urllib.request import urlopen


def sync_get_url(url):
    return urlopen(url).read()


async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    responce = await future
    print(len(responce))


loop = asyncio.get_event_loop()
r = loop.run_until_complete(load_url("https://www.google.com/", loop=loop))
