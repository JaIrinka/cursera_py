# *****************************
#    ПЕРЕМЕННЫЕ В ПРОЦЕССАХ
# *****************************
import os

foo = 'bar'
pid = os.fork()

if pid == 0:
    foo = 'baz'
    print(f'child: {foo}')
else:
    print(f'parent: {foo}')
    os.wait()
