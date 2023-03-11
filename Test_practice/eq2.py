#Write a python program to print sum of digit using given number.
#logic ; number = 1634 = [1+6+3+4] =14
number = int(input("Enter a number: "))
sum = 0
while(number>0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("The sum is,",sum)
