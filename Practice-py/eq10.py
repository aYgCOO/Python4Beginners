#Check the number is palendrim or not;
num = int(input("Enter a number: "))
temp = num
count = 0

while(num>0):
    digit = num%10
    count = count*10 + digit
    num = num //10
if(count==temp):
    print("Its a palindrom number.")
else:
    print("Its not a palindrom number.")
