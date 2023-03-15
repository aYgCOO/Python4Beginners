# Practice 1 ;
# There are 6 subjects ,1)Physics 2)Chemistry 3)Biology 4)Computer_Application 5)English 6)Bengali ;
physics = int(input("Enter your Physics's marks: "))
chemistry = int(input("Enter your Chemistry's marks: "))
biology = int(input("Enter your Biology's marks: "))
complication = int(input("Enter your Computer_Apllication's marks: "))
english = int(input("Enter your English's marks: "))
bengali = int(input("Enter your Bengali's marks: "))
avg = (physics+chemistry+biology+complication+english+bengali)/600
avg = avg * 100
if (avg >= 100):
    print("GRADE AA")
elif (avg > 90):
    print("GRADE A+")
elif (avg > 80):
    print("GRADE A")
elif (avg > 75):
    print("GRADE B+")
elif (avg > 65):
    print("GRADE B")
elif (avg > 55):
    print("GRADE C+")
elif (avg > 45):
    print("GRADE C")
elif (avg > 30):
    print("GRADE D")
else:
    print("Fail , now you fuck your self....")