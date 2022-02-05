# *****************************
#      ФАЙЛЫ В ПРОЦЕССАХ
# *****************************
import os

file = open('data')
foo = file.readline()

if os.fork() == 0:
    foo = file.readline()
    print(f'child: {foo}')
else:
    foo = file.readline()
    print(f'parent: {foo}')
    os.wait()
