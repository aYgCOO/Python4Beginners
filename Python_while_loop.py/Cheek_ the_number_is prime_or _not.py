lag = 0
num = int(input('\nEnter whole number to check : '))
i = 2
while i <= (num/2):
    if (num%i) == 0:
        flag = 1
        break
    else:
        i += 1
    
if num == 1:
    print('1 is neither prime nor composite')
elif flag == 0:
    print(num,' is a prime number.')
elif flag == 1:
    print(num,' is not a prime number.')