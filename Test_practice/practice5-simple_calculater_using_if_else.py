#Practice 5;
# Create a simple calculater using if else;
c = int(input("1)Addition , 2)Substraction , 3)Multiplcation , 4)Division , 5)Exponiantiol , 6)Floor_Division ;   Enter your choice: "))
if (c==1):
    x = int(input("Enter your first value: "))
    y = int(input("Enter your second value: "))
    print("Addition=",x+y)
elif (c==2):
    x = int(input("Enter your first value: "))
    y = int(input("Enter your second value: "))
    print("Subtraction=",x-y)
elif (c==3):
    x = int(input("Enter your first value: "))
    y = int(input("Enter your second value: "))
    print("Multiplcation=",x*y)
elif (c==4):
    x = int(input("Enter your first value: "))
    y = int(input("Enter your second value: "))
    print("Division=",x/y)
elif (c==5):
    x = int(input("Enter your first value: "))
    y = int(input("Enter your second value: "))
    print("Exponiantiol=",x**y)
elif (c==6):
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print("Floor_Division=",x//y)
else:
    print("Error!")


