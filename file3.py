with open("codingal.txt","w") as file:
     file.write("Hi my name is Sahasra I am  11 years old\n")
file.close()

with open("codingal.txt","r") as file:
    a = file.readlines()
    for i in a:
        data=i.split()
        print(data)
file.close()

# newfile = open("sahasra.txt","x") 

import os
if os.path.exists("abc.txt"):
   os.remove("abc.txt")
else:
    print("There is no such file/1")

file = open("codingal.txt","a")
file.write("Hi my school name is Guru \n My school has a playgrounthere are many students an teachers\n We have many subjects in our school\n" )
file.write("My hobbies are styuding,attending classes.listening to music")


       
   


