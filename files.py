file = open("abc.txt","w")
file.write("Hello my name is Sahasra i am styuding in grade 6")
file.close()

file1 = open("abc.txt","r")
print(file1.read())
file1.close()

file2 = open("abc.txt ","a")
file2.write( " I love coding i am learning python")
file2.close