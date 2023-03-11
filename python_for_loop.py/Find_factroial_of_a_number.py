num=int(input("Enter a number: "))
fact=1
if num<0:
    print("Its not a factroial number.")
if num==0:
    print("Factroial of 0 is.",1)
if num>0:
    for i in range(1, num+1):
            fact=fact*i
print("The factroial of given number is.",fact)
