#Hill partten ;
n=1000

print()

for i in range(n):
    for j in range(i,n):
        print(" ",end='')

    for j in range(i):
        print("_",end='')

    for j in range(i+1):
        print("_",end='')
    print()