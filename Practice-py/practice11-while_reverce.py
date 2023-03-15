#Practice11;
#While loop;
b = int(input("Enter a number: "))
i = 0
while (b>i):
    print(i)
    i+=1 #(Manwali increment;)


#While loop reverce;

num = int(input("Enter a number: "))
rev=0
while (num!=0):
    digit = num % 10
    rev = rev*10 + digit
    num = num//10
print("Reverse=",rev)

