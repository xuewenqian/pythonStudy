
class student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2015-self._birth
x=student()
x.birth=5
print(x.birth)
print(x.age)

class Student2(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
y=Student2()
y.score(20)
print(y.score)
