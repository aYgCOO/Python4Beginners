n = 10

print()

for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    for j in range(i + 1):
        print("_", end=' ')
    print()


print()

print()

for i in range(n):
    for j in range(i+1):
        print("_", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()