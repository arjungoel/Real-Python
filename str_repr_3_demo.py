class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __repr__(self):
        return '{self.__class__.__name__} ({self.color},{self.mileage})'.format(self=self) # calls the __repr__ internally


my_car = Car('red',13450)
print(my_car)
print(str(my_car))

# how containers convert their child objects or the objects they contain to string?
# If you call __str__ on containers then it's going to represent the internal objects with the __repr__ function.

# Atleast add a __repr__ method to your classes.