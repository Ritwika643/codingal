import matplotlib.pylot as plt

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