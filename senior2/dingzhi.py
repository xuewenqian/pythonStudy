

print('*****__str__*****')
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__=__str__
print(Student('michael'))

print('*****__iter__*****')
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration();
        return self.a
for n in Fib():
    print(n)
    
    
print('*****getitem*****')
class fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
f=fib()
#print(f[0])
#print(f[1])
print(f[100])
print(f[1:15])


print('*****__getattr__*****')
class student2(object):
    def __init__(self):
        self.name='xue'
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)
s=student2()
print(s.name)
print(s.score)
print(s.age)

print('*****getattr应用：动态属性*****')
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
print(Chain().status.user.timeline.list)

print('*****__call__*****')

class Student3(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('my name is %s' % self.name)
s=Student3('xue')
s()


print(callable(max))
print(callable(s))
print(callable([1,2,3]))
















