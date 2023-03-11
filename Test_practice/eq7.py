#Fibonacci series ;
#logic; 0 , 1, 1 , 2 , 3, 5 , 8..........
#using for loop:
num = int(input("Enter a number: "))
first = 0
second = 1
for i in range(0,num):
    print(first)
    temp = first
    first = second
    second = temp + second



    
