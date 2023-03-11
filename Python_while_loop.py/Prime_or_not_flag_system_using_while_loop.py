n = int(input("Enter a number: "))
flag = True
num = 2
while (n<num):
    if n%num == 0:
        flag = False
if flag == True:
    print(n,"<--The number is an prime number.")
else:
    print(n,"<--The number is not an prime number.") 