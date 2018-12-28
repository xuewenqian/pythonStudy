from functools import reduce
def add(x,y):
    return x*10+y
result=reduce(add,[1,3,5,7,9])
print(result)

print('-----将str转换为int-----')
print('---版本一---')
def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
result=reduce(fn,map(char2num,'13579'))
print(result)

print('---版本二---')
def str2int(s):
    def fn(x,y):
	    return x*10+y
    def char2num(s):
	    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
print(str2int('1234'))

print('---版本三lambda---')
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('567'))


