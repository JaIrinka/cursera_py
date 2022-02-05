# *****************************
#         ПУЛ ПОТОКОВ
# concurrent.futures.Future
#
# https://docs.python.org/3/library/concurrent.futures.html
# *****************************
from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


# вспоминаем тему "контекстные менеджеры"
# .shutdown() in exit
# то есть, по идее, это можно использовать без with
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
