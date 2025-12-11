#Activity - 1 -- 0(1)Time
def printnumber(n):
    literation = 0 
    print("total umber entered is:", n)
    literation += 1
    print("total literation is:", literation, "\n")
    printnumber(10)
    printnumber(200)
    print("\n Activity - 1 with any 'n' time will not change")

#Activity - 2 -- 0(n) Time

def Ontime(n):
    iteration = 0
    for i in range(1, n+1):
        iteration += 1
        print("Activity - 3 -- \n when n is ", n , " iteration is: ", iteration)

Ontime(5)
Ontime(10)
Ontime(15)
Ontime(20)

#Activity - 3 -- 0(n^2) Time
def test(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print('*', end=' ')
            iteration += 1
            print('')
            print("\nwhen n is ", n , " iteration is: ", iteration)
test(5)
test(4)
test(3)
print("\n Activity - 3 with any 'n' time will change according to n^2")
print("(n^2)")