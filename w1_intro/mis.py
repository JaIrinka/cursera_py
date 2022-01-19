#import this
#import inspect
#import os

#import requests
#import pprint

from mypackage.utils import *
import dis
import opcode

print(multiply.__code__.co_code)
print(dis.dis(multiply))
print(opcode.opmap)

#def get_location_info():
#    return requests.get("http://ip-api.com/json/").json()

#if __name__ == "__main__":
#    pprint.pprint(get_location_info())
#    n = 1

#print(multiply(2, 3))


#print(f'aaaaaa {inspect.getfile(this)}')
#print(os.listdir("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8"))
