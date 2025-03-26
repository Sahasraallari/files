file = open("pqr.txt","r")
count=0
a=file.read()
b=a.split("\n")
for i in b:
    if i:
        count=count+1
print("This is the number of line in file")
print(count)

