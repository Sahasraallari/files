file = open("test.txt","w")
file.write("I Love coding")
file.write("\n")
file.write("I love Html")
file.write("\n")
file.write("I Love Css")
file.write("\n")
file.write("I Love Python")
file.write("\n")
file.write("I Love Bootstrap")
file.write("\n")
file.write("I Love Java")
file.write("\n")
file.write("I Love Bookclub")
file.close()

file1 = open("test.txt","r")
print(file1.read(8))
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
file1.close()

file2 = open("test.txt","r")
for a in file2:
    print(a)
file2.close()
