import types

print(type(123))
print(type('str'))
print(type(None))

print(type(abs))

print(type(123)==type(345))

print(type(123)==int)

def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#print(dir('abc'))

class mydog(object):
    def __len__(self):
        return 100

dog=mydog()
print(len(dog))

print('ABC'.lower())

class myObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=myObject()
print(hasattr(obj,'x'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))

print(hasattr(obj,'power'))
print(getattr(obj,'power'))



