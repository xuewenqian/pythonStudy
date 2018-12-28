def count():
    fs=[]
    for i in range(1,3):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2=count()
print(f1)
print(f2)
#print(f3)

print(f1())
print(f2())
#print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())