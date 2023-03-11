#check the number is amstrong or not using while loop ;
#logic 1634 = [1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4]
num = int(input("Enter a number: "))
num_str=str(num)
temp = num
count = 0
while(num>0):
    digit = num%10
    count = count + digit**len(num_str)
    num = num//10
if(temp==count):
    print("The number is an amstrong number.")
else:
    print("The number is not an amstrong number.")

