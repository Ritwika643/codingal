#Activity - 1
def power2(number):
    if number == 0:
        return 0
    if (number & (-(number - 1))) == number:
        return 1

    return 0
number = int(input("Enter a number: ")) 
if power2(number):
    print("yes")
else:
    print("no")

#Activity - 2
def  powerof4(number):
    count = 0
    if number == 0:
        return 0
    while number > 1:
        number>>=1
        count += 1
    if count%2 == 0:
        return 1
    else:
        return 0
number = int(input("Enter a number: "))
if powerof4(number):
    print("yes")
    print("power of 4")
else:
    print("no")
    
#Activity - 3 - Lon(n)power
def computerpower(x,y):
    result=1
    while y>0:
        if y%2==1:
            x=x*x
            y=y//2
        else:
            result=result*x
            y>>=1
    return result
x=int(input("Enter the base number: "))
y=int(input("Enter the power: "))
print("The result is:",computerpower(x,y))