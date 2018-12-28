#class Student(object):
#    pass
#bart=Student()
#print(bart)
#print(Student)

#bart.name='xue'
#print(bart.name)


class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score
        
bart=Student('xue',59)
print(bart.get_name(),bart.get_score())
bart.set_name('qian')
bart.set_score(70)
print(bart.get_name(),bart.get_score())

print(bart._Student__name)
print(bart._Student__score)

#bart.print_score()
#print(bart.get_grade())

#lisa=Student('lisa simpson',87)
#bart.age=19
#print(bart.age)
#print(lisa.age)

#print(bart.__name)