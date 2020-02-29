# How Python class is represented as a string and also when you interact with it or inspected in a Python Interpreter
# session?
# How does dunder __str__ and __repr__ work?
# Classes are not supposed to actually define their own dunder methods because they could conflict with Python
# features in the future.
# The way you would actually convert an object to a string can be done as str(object) and it is going to call the
# __str__ method internally.
# By convention if you call the __str__ method, then it is going to do lot of good things for you in controlling how
# your object is represented with or represented as a string, so it's the pythonic way to do this.

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return 'a {self.color} car'.format(self=self)
    
my_car = Car('red', 12000)
# print Car object.
print(my_car)
print(str(my_car))

print('{}'.format(my_car))  # it will also called the __str__ represent the same output

# How does __repr__ works and is different from __str__?

