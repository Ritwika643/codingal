num1 = 10
num2 = 4
print("num1 & num2 =", num1 , num2)
print("num1 | num2 =", num1 | num2)
print("num1 ^ num2 =", num1 ^ num2)
print("num1 >> num2 =", num1 >> num2)
print("num1 << num2 =", num1 << num2)
print("~num1 =", ~num1)
print("~num2 =", ~num2)

def isEvenOdd(number):
    if ( n ^ 1) == number + 1:
        return True
    else:
        return False
        
number = int(input("Enter a number to check even or odd: "))
if isEvenOdd(number):
    print(number, "is even")
else:
    print(number, "is odd")

def isEvenOddAnd(number):
    if (number & 1) == 0:
        return True
    else:
        return False
number = int(input("Enter a number to check even or odd using AND operator: "))
if isEvenOddAnd(number):
    print(number, "is even")
else:
    print(number, "is odd")