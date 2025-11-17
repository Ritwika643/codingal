#Activity-1
file=open("demo.txt","r")
print(file.read())

#Activity-2 & 4
file=open("demo.txt")
print(file.read())
file.close()
file_append=open("demo.txt","a")
file_append.write("this is appended line")
file.append.close()

#Activity-3
file=open("demo.txt")
counter = 0
content=file.read()
coList=content.split("\n")
for i in coList:
    if i:
        counter+=1
print("Number of lines:",counter)