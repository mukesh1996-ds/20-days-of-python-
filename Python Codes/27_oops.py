class Car:

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"
Honda = Car(24.1,"Honda City")
print(Honda.description())

# Example of inherited in class 

class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."
obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())

"""
We have created two child classes, namely “BMW” and “Audi,” who have inherited the methods and 
properties of the parent class “Car.”  We have provided no additional features and methods in the 
class BMW. Whereas one additional method inside the class Audi.

Notice how the instance method description() of the parent class is accessible by the objects of 
child classes with the help of obj1.description() and obj2.description(). The separate method of 
class Audi is also accessible using obj2.audi_desc().
"""

# Encapsulation 

class car:

    def __init__(self, name, mileage):
        self._name = name                #protected variable
        self.mileage = mileage 

    def description(self):                
        return f"The {self._name} car gives the mileage of {self.mileage}km/l"
obj = car("BMW 7-series",39.53)

#accessing protected variable via class method 
print(obj.description())


class Car:

    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
obj = Car("BMW 7-series",39.53)

#accessing private variable via class method 
print(obj.description())


class Car:

    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
obj = Car("BMW 7-series",39.53)

#accessing private variable via class method 
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj._Car__name)      #mangled name

"""
Note that the mangling rule’s design mostly avoids accidents. But it is still possible to access 
or modify a variable that is considered private. 
This can even be useful in special circumstances, such as in the debugger.
"""

#accessing protected variable directly from outside
print(obj._name)
print(obj.mileage)

## Polymorphism

class Audi:
  def description(self):
    print("This the description function of class AUDI.")

class BMW:
  def description(self):
    print("This the description function of class BMW.")
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
 car.description()

"""
When the function is called using the object audi then the function of class Audi is called, 
and when it is called using the object bmw, the function of class BMW is called.
"""

