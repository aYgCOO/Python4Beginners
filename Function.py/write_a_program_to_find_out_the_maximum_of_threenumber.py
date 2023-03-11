def maximum(a,b,c):
    if (a>=b) and (a>=c):
        largest = a
    elif (b>=a) and (b>=c):
        largest = b
    else:
        largest = c
         
    return largest

# Arguments.....
a=124
b=8989
c=999
print("The largest number is....", maximum(a,b,c))





