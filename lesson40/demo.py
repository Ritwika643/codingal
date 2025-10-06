# def intro(name):
#     print(f"Hello, {name}!")
#     print("What are you doing?")
#     print("I am learning Python.")

#     intro("Alice")
#     intro("Bob")
#     intro("Charlie")
#     intro("ritwika")


# def intro2(name, age , city):
#         return f"Hello, {name}! i am {age} years old and live in {city}."
# result = intro2("Alice", 30, "New York")
# print (result)

def intro3(count):
    if (count == 200):
        return
    
    print(f"Hello, count is {count}")
    count = count + 1
    intro3(count)

intro3(0)