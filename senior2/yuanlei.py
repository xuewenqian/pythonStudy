class Hello(object):
    def hello(self,name='world'):
        print('hello,%s.'%name)
        
        
print('*****通过type创建对象*****')
def fn(self,name='world'):
    print('hello,%s.'%name)
Hello2=type('Hello2',(object,),dict(hello=fn))
h=Hello2()
h.hello()
print(type(Hello2))
print(type(h))