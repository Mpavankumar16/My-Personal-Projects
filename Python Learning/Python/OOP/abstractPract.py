#ABC - Abstract Base Class
from abc import ABC, abstractmethod

#Abstract class can't be instantiated
class Vehicle(ABC):
    @abstractmethod
    def type(self):
        pass

#As I'm inheriting abstract class I need to implement all it's methods
class Car(Vehicle):
    def type(self):
        print("I'm a car")

class Bike(Vehicle):
    def type(self):
        print("I'm a Bike")
   