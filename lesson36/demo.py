a = 5
#integer type
b = 3.14
#float type
c = "hello"
#string type
d = True
#boolean type
e = False
#NoneType
f = '56'
#string type

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

a = str(a)
b = int(b)
d = str(d)
e = float(e)
f = bool(f)
print(f"a is {a} and its type is {type(a)}")
print(f"b is {b} and its type is {type(b)}")
print(f"c is {c} and its type is {type(c)}")
print(f"d is {d} and its type is {type(d)}")
print(f"e is {e} and its type is {type(e)}")
print(f"f is {f} and its type is {type(f)}")
a = int(a)
b = float(b)
res = 54 + a / b * 43 - 2 % 4 // 35 ** 2
print(res)
print(15 % 4)
print(15 / 4)
print(15 // 4)
z = input("enter a number: ")
print(z)
