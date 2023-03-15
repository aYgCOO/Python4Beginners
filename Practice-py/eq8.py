#Fibonaci series using while loop ;
#logic; 0 , 1 ,1 ,2,3,5,8.........
num = int(input("Enter a number: "))
first = 0
second = 1
sum = 0
if (num<0):
    print("Please enter a positive number.")
elif (num==1):
    print("Fibonacci sequence upto.")
else:
    print("Fibonacci sequence")
    while(sum<num):
        print(first)
        temp = first
        first = second
        second = temp + second
        sum+=1
