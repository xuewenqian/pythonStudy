def is_odd(s):
    return s%2==0
result=list(filter(is_odd,[1,2,3,4,5]))
print(result)

def not_empty(s):
    return s and s.strip()
result=list(filter(not_empty,['a','','b',None,'d']))
print(result)

print('-----用filter来筛选素数-----')

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

		
for n in primes():
    if n<1000:
	    print(n)
    else:
        break

print('-----用filter来筛选素数-----')