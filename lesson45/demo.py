class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(f"This car is a {self.color} {self.brand}.")

car1 = Car("Toyota", "Red")
car1.show()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s1=Student("Amit",80)
print(s1.name)
print(s1.marks)

#Types of Inheritance

#1.Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")

#2. Multi-level Inheritance
class Father:
    def quality(self):
        print("Honest and hardworking")
class Mother:
    def quality(self):
        print("Caring and loving")
class Child(Father, Mother):
    def talent(self):
        print("Singing and dancing")
c=Child()
c.quality()
c.talent()
