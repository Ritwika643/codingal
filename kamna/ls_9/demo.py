number = int(input("enter"))
result = 0
temp = number
while temp!= 0:
    digit = temp % 10
    result + digit ** 3
    temp = temp // 10
    print(result)
if result == number:
    print (number, "is an Armstrong number")
else:
    print (number, "is not an Armstrong number")

number = int(input("enter a number: "))
s = 0
temp = number
while temp!= 0:
    digit = temp % 10
    s = s + digit ** 3
    temp = temp // 10
    if number == s:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")


def roman_to_integer(a):
    roman_numerals = {
        'I': 1,'V': 5,'X': 10,'L': 50,'C' : 100,'D' : 500,'M': 1000}
    int_form = 0
    for i in range(len(a)):
        if i + 1 < len(a) and roman_numerals[a[i]] < roman_numerals[a[i + 1]]:
            int_form -= roman_numerals[a[i]]
        else:
            int_form += roman_numerals[a[i]]
    return int_form
a = input("Enter a roman numeral: ")
print("The integer form is:",a, roman_to_integer(a))