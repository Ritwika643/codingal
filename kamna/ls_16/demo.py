#Activity - 1
def swap1(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
print("After swapping : a =", a ,"b =", b)

def swap2(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
print("After swapping : a =", a ,"b =", b)

swap1(5, 10)
swap2(3, 9)

#Activity - 2
def divide(ourDividend, ourDivisor):
    sign = (-1 if (ourDividend < 0) ^ 
                        (ourDivisor < 0) else 1)
    
    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)
    quotientnumber = 0
    tempnumber = 0

    for i in range(31, -1, -1):
        if tempnumber + (ourDivisor << i) <= ourDividend:
            tempnumber += ourDivisor << i
            quotientnumber |= 1 << i

    if sign == -1:
        quotientnumber = -quotientnumber
    return quotientnumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("Quotient of a/b is: ", divide(a, b))