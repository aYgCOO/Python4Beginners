num=int(input("Enter a number: "))
n1,n2=0,1
sum=0
if (num<=0):
    print("Please enter a positive number.")
elif (num==1):
    print("Fibonacci sequence upto.")
else:
    print("Fibonacci sequence.")
    while(sum<num):
        print(n1)
        no=n1+n2
        n1=n2
        n2=no
        sum+=1