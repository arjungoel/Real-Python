class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __repr__(self):
        return '__repr__ for Car'
    def __str__(self):
        return '__str__ for Car'
    
my_car = Car('red', 12000)

print(my_car)
print('{}'.format(my_car))