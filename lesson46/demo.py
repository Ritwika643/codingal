class Student:
    def __init__(self, name, marks):
        self.name = name #public variable
        self.__marks = marks #private variable (hidden)

        def get_marks(self):
            return self.__marks
        
        def set_marks(self, marks):
         if  marks>=0 and marks<=100:
            self.__marks = marks
         else:
            print("Invalid marks!")

s1=Student("Mani", 25)
s2=Student("Kumar", 45)
s3=Student("Vaibhav", 85)

#print("name",s1.name)  

#print("marks",s1.get_marks())

#s1.set_marks(95)

#print("Updated marks",s1.get_marks())

print("Marks of s2:",s2.get_marks())
