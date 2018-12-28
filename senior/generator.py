L=[x*x for x in range(10)]
print(L)

g=(x*x for x in range(10))
print(g)
print(next(g))

for n in g:
    print(n,2)
	

print('-----斐波那契数列-----')

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(5))
print(next(fib(5)))

print('-----斐波那契数列-----')

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o=odd()
print(next(o))
print(next(o))
print(next(o))
print(next(o))


