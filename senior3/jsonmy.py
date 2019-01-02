import json
d=dict(name='bob',age=20,score=88)
s=json.dumps(d)
print(s)

#json 对象 之间转换
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
a=Student('xue',28,99)
print(json.dumps(a,default=student2dict))