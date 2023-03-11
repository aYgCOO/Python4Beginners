n=int(input("Enter a number: "))
if(n<0):
    print("Enter positive number: ")
else:
    sum=0
    while(n>0):
        sum = n + sum
        n = n - 1
        print("Sum of n natural is",sum)
