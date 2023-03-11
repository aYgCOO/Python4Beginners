num = int(input("Enter a number: "))

print()

for row in range(1,num+1):
    for colum in range(1,row+1):
        print("%",end=' ')
    print()
for row in range(num-1,0,-1):
    for colum in range(1,row+1):
        print("&",end=' ')
    print()