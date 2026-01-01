#Acrtivity - 1 ONES AND ZEROS
def numberOfBits(n):
    ones = 0
    zeros = 0
    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeros += 1
            n >>= 1
            print("Number of ones are: ", ones , "Number of zeros are: ", zeros)
number = int(input("Enter a number: "))
numberOfBits(number)

#Activity - 2 nth bit set or not
def setOrNot(number, n):
   #define mask before use 
    mask = 1 #assuming  to check if the bit is set or not
    if (n & mask) == 1 or (n & mask) == 0: #corrected comparison
        if number & (1 << (n - 1)):
            print("SET")
        else:
            print("NOT SET")
    number = int(input("Enter a number: "))
    n = int(input("Enter the position of bit to check: "))       
    setOrNot(number, n)