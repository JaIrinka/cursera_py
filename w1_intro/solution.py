import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


sqrt_D = (b**2 - 4*a*c)**(1/2)
print(int((-b+sqrt_D)/(2*a)))
print(int((-b-sqrt_D)/(2*a)))
