from types import MethodType

class Student(object):
    pass
    
s=Student()
s.name='xue'
print(s.name)

def set_age(self,age):
    self.age=age
def set_score(self, score):
    self.score = score

#s.set_age=MethodType(set_age,s)
#s.set_age(25)
#print(s.age)

Student.set_score=MethodType(set_score,Student)

s2=Student()
s2.set_score(21)
print(s2.score)


class Student1(object):
    __slots__=('name','age')
    
x=Student1()
x.name='xue'
print(x.name)
x.age=22
print(x.age)
#x.score=12
#print(x.score)


class graduateStudent(Student1):
    pass
y=graduateStudent()
y.score=90
print(y.score)
    
