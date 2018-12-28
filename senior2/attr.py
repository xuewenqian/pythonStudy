
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student('xue')
s.score=90
print(s.name)
print(s.score)


class Student(object):
    name='student'

s=Student()
print(s.name)
print(Student.name)

s.name='xue'
print(s.name)
print(Student.name)