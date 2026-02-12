print("what is the type of database /n 1. Relational Database /n 2. NoSQL Database")
answer = input("Enter your choice (1 or 2): ")
if answer == '2':
    print("NoSQL databases are non-relational databases that store data in a flexible, schema-less format. They are designed to handle large volumes of unstructured or semi-structured data and are often used for big data applications, real-time web applications, and distributed systems.")
else:
    print("Relational databases are structured databases that store data in tables with predefined schemas. They use SQL (Structured Query Language) for querying and managing data. Relational databases are suitable for applications that require complex queries, transactions, and data integrity.")
print ("try again ")