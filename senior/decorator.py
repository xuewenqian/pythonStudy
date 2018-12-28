import functools
def log2(text):
    def decorator(func):
        @functoos.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

def log1(func):
    @functoos.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log2('execute')
def now():
    print('xue')
f=now
f()

print(now.__name__)
print(f.__name__)


