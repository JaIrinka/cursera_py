# *****************************
# проверяю, можно ли использовать связку fork+wait как замыкание
#
# оказалось что можно. wait ждёт всех
# *****************************
import os
import time
import random

n = 5
is_parent = True

for i in range(n):
    pid = os.fork()
    if pid == 0:
        is_parent = False
        sleep_time = random.randint(3, 10)
        time.sleep(sleep_time)
        print(f'continue {os.getpid()}, work time {sleep_time}')
        quit()

    print('pizda', pid)

while n > 0:
    os.wait()
    time.sleep(1)
    n -= 1
    print(f'something continued, waiting for {n}')





