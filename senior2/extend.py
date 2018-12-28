class Animal(object):
    def run(self):
        print('Animal is running...')

class dog(Animal):
    def run(self):
        print('dog is running...')
    def eat(self):
        print('eating meat...')
    
class cat(Animal):
    def run(self):
        print('cat is runnning...')
        
class tortoise(Animal):
    def run(self):
        print('tortoise is running slowly...')

dog1=dog()
cat1=cat()

dog1.run()
cat1.run()


print('-----多态-----')

a=list()
b=Animal()
c=dog()

print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,dog))
print(isinstance(c,Animal))
print(isinstance(b,dog))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(dog())
run_twice(tortoise())

print('-----多态-----')