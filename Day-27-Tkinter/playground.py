def add(*args):
    return sum(args)


print(add(3,5,6))

print(add(3,5,6, 2, 1, 7, 4,3))


def calculate(n, **kwargs):
    print(kwargs)
    
    # for key, value in kwargs.items():
    #     pass
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    


calculate(2, add=3, multiply=5)
        
        
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)