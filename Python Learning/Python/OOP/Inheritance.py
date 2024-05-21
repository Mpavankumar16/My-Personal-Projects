class Organism:
    alive = True

#Multi level inheritance
class Animal(Organism):
    alive = False

    def eat(self):
        print("I'm eating")
    
    def sleep(self):
        print("I'm sleeping")
    
#Inheritance
class Dog(Animal):
    pass

dog1 = Dog()
print(dog1.alive)
dog1.eat()


#Multiple Inheritance

class RBI:
    def eligibility(self):
        print("Take only aadhar")
    
class SEBI:
    def eligibility(self):
        print("Take aadhar and PAN")

class myBank(RBI, SEBI):
    pass

myB = myBank()
myB.eligibility()