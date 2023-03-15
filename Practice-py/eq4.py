# print the buzz number in 1 to 100;
def is_buzz(num):
    return num % 7==0 or "7" in str(num)
    
for i in range(1,101):
    if is_buzz(i):
        print(i,end=",")
