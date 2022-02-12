# *****************************
#        ASYNCIO. КЛИЕНТ
# *****************************
import asyncio


async def tcp_echo_client(msg):
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001)

    print(f"send: {msg}")
    writer.write(msg.encode())
    writer.close()


loop = asyncio.get_event_loop()
message = "hello World!!!!"
# передавать loop больше не надо, мы и так вызываем корутину внутки метода из loop
loop.run_until_complete(tcp_echo_client(message))
loop.close()
