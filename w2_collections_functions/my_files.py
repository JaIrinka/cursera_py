#*****************************
#          ФАЙЛЫ
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# modes
# r = read
# w = write
# a = add
# r+ = read + write
#*****************************

f = open('testfile', 'r+')
f.write('LOTR\nLord Of The Rings')
f.close()


with open('testfile', 'r+') as f:
    print(f.read())
