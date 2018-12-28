#def person(name,age,**kw):
#    print('name:',name,'age:',age,'other',kw)
#person('xue','29')
#person('xue','20',city='beijing')
#person('xue','20',city='beijing',firstname='wen')
#
#extra={'city':'Beijing','job':'Engineer'}
#person('jack','24',**extra)


print('-----命名关键字参数-----')
def person(name,age,**kw):
    if 'city' in kw:
	    print('has city param')
    if 'job' in kw:
	    print('has job param')
    print('name:',name,'age:',age,'other:',kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
print('-----命名关键字参数-----')
