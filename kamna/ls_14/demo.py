#Activity - 1
def checkIfsame(number1, number2):
    if ((number1 ^ number2)!= 0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
checkIfsame(number1, number2)

#OneOddOccurring
def OddOccurring(arr):
    res = 0
    for element in arr:
        res = res ^ element
        return res
    arr = []
    n = int(input("Enter array size: "))
    while (n):
        num = int(input("Enter number: "))
        arr.append(num)
        n -= 1
    print("The odd occurring element is: ", OddOccurring(arr))

    #TwoOddOccurring

def TwoOdd(arr,size):
    xorof2 = arr[0]
    x = 0
    y = 0
    Setbit = 0
    for i in range(1,size):
        xorof2 = xorof2 ^ arr[i]
    Setbit = xorof2 & ~(xorof2 - 1)
    for i in range(size):
        if (arr[i] & Setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("The two odd occurring elements are: ", x, " and ", y)
    arr = []
    arr_size = int(input("Enter array size: "))
    for i in range(0,arr_size):
        z = int(input("Enter number: "))
        arr.append(z)
    print("TwoOdd")