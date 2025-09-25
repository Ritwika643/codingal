a = 60 

if a > 40:
    print(a*90)
    print("a is greater than 40")
    if a/40==2:
        print("a is divided by 40 is 2")
        else:
        print("a is divided by 40 is not 2")
elif a < 50:
    print("timepass")
else:
    print(a*20)
    print("a is less than 40")

import datetime 
currenttime = datetime.datetime.now()
print(currenttime)

import calendar
print(calendar.calendar(2025))