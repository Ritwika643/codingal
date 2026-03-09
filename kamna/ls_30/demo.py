data_type = [("name", "S10"), ("class", int), ("height", float)]
students_details = [("Alice", 10, 5.5), ("Bob", 9, 5.8), ("Charlie", 10, 5.6)]
students = np.array(students_details, dtype=data_type)
print("Original_array")
print(students)
print("Sorted by height")
sorted_students = np.sort(students, order="height")
print("Sorted by name")
sorted_students = np.sort(students, order="name")
print("Sorted by class")
sorted_students = np.sort(students, order="class")