#GCD(HCF/GCD)
smallNum = int(input("Enter the smaller number: "))
largeNum = int(input("Enter the larger number: "))
while smallNum != 0:
    remainder = largeNum % smallNum
    largeNum = smallNum
    smallNum = remainder
print("The GCD is:", largeNum)
#Palindrome
number = int(input("Enter a number: "))
original_num = number
reversed_num = 0
# Reversing the number
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

if original_num == reversed_num:
        print(original_num, "is a palindrome")
else:
        print(original_num, "is not a palindrome")