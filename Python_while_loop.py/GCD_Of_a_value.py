a = float(input("Please Enter the first value a: "))
b = float(input("Please Enter the second value b: "))
i = 1
while (i<a and i<b):
    if (a%i == 0 and b%i == 0):
        gcd =i
        i=i+1
    print("\n GCD is ....",gcd)