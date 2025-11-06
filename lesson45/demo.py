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