from collections import Iterable

d={'a':1,'b':2,'c':3}
for x in d.values():
    print(x)
	
for ch in 'xuewenqian':
    print(ch)
	
print('-----判断一个对象是否为可迭代对象-----')
print(isinstance('avc',Iterable))

for i,value in enumerate(['a','b','c']):
    print(i,value)