import matplotlib.pyplot as plt

student_names = ["sanjay", "rahul", "karan" , "wasim" , "ramesh" , "ajay", 'sartaj']
student_marks = [90, 80, 70, 60, 50, 40, 30] 

marks_per = []
for x in student_marks:
    res = (x / 50) * 100
    marks_per.append(res)

print(marks_per)
#line graph
def marks_line_graph(student_names, marks_per):
    plt.plot(student_names, marks_per)
    plt.xlabel("Student Names")
    plt.ylabel("Marks Percentage")
    plt.title("Student Marks Line Graph")
    plt.show()

marks_line_graph()

#bar graph
def percentage_bar_graph(student_names, marks_per):
    plt.bar(student_names, marks_per)
    plt.xlabel("Student Names")
    plt.ylabel("Marks Percentage")
    plt.title("Student Marks Bar Graph")
    plt.show()
percentage_bar_graph()
import matplotlib.pyplot as plt

fruit_names= ['apple','mango','watermelon','dragonfruit','banana']
fruit_cost=['250','520','300','110','320']

print(fruit_cost)

def cost_line_graph(cost, name):
 plt.plot (cost , name)
 plt.xlabel('cost of 1 fruit')
 plt.ylabel('name of the fruit')