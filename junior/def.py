def my_abs(x):
    if not isinstance(x,(int,float)):
	    raise TabError('bad operand type')
    if x>0:
	    return x
    else:
	    return -x
print(my_abs(-5))

def nop():
    pass
print(nop())

import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
	
x,y=move(100,100,60,math.pi/6)
print(x)
print(x,y)

r=move(100,100,60,math.pi/6)
print(r)

#默认函数#
print("-----默认函数-----")
def power(x,n=2):
    s=1
    while n>0:
	    n=n-1
	    s=s*x
    return s
print(power(5))
print(power(5,3))
print("-----默认函数-----")
