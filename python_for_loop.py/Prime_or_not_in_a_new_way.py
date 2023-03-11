num = int(input("Enter a number: "))
flag = True
for i in range(num,1):
    if num%i == 0:
        flag = False
if flag == True:
    print("Its a prime number.")
else:
    print("Its not a prime number.")
