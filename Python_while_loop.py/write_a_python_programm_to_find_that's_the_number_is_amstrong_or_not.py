n=int(input("Enter a number: "))
temp=n
formula=0
while (n>0):
    rem=n%10
    formula=(formula+rem)**3
    n=n//10
if (temp==formula):
    print("Its a Amstrong number.")
else:
    print("Its not a Amstrong number.")