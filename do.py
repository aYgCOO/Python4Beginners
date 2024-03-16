#Do while loop
'''In Python, there isn't a direct equivalent of a do-while loop like in some other programming languages.
 However, you can achieve similar functionality using a while loop with a condition that is initially True, 
 and then you break out of the loop when a certain condition is met. This gives the effect of executing 
 the loop body at least once, similar to a do-while loop.'''

i = 0
while True:
     print(i)
     i += 1
     if(i>=10):
          break
