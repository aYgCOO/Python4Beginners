#eq1;
#Write a suitible program to check a user given number is Amstrong or not using python;
#I use the function;
#logic , number = 1634 [1*1*1*1*+6*6*6*6+3*3*3*3+4*4*4*4] = 1634
number = int(input("Enter a number: "))
def check_amstrong(num):
    if num in range(1,1001):
        return True
    count = len(str(num))
    sum = 0
    temp = num
    while (num>0):
        digit = num % 10
        sum = sum + digit**count
        num = num//10
    if (sum == temp):
        return True
    return False
if check_amstrong(number):
        print("Number is an amstrong number.")
else:
     print("Number is not an amstrong number.")

