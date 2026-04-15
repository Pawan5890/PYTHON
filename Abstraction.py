#Abstract Class
#It is used to force child classes to implement methods
#Abstract class object can't be created

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class cat(Animal):
    def sound(self):
        print("Meow")
    def eat(self):
        print("Eating bread")

d=Dog()
d.sound()
c=cat()
c.sound()
c.eat()
