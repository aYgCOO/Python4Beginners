#Write a calculater and create an advance choice calculater using python

'''Atfirst we need to take some inputs choice from user'''
print("\n You can by default use two operend to calculate an equation or you can use maximum of 6 operend to calculate an equation.")
while(True):
   how_many_inputs = int(input("How many inputes you need \n One('Default',1) Two(2) \n Three(3) \n Four(4) \n Five(5) \n Six(6) \n Exit(0) \n  ::"))
   if(how_many_inputs == 0):
     print("Are you sure? \n Do you want to exit?")
     programm_exit = str(input("Yes(1) || No(2) \n ::"))
     if(programm_exit == '1'):
       print("Exit.......")
       break
     else:
       print("Continue....")
       continue
   elif(how_many_inputs == 1 or how_many_inputs == 2):
     inp_1 = int(input("Enter the first number: "))
     inp_2 = int(input("Enter the second number: "))
     while(True):
       choice = str(input("Choose your operator \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Divission(/) \n :: "))
       if(choice == '+'):
         add = inp_1 + inp_2
         print(add)
         break
       elif(choice == '-'):
         sub = inp_1 - inp_2
         print(sub)
         break
       elif(choice == '*'):
         mul = inp_1 * inp_2
         print(mul)
         break
       elif(choice == '/'):
         div = inp_1 / inp_2
         print(div)
         break
       elif(choice == '%'):
         mod = inp_1 % inp_2
         print(mod)
         break 
       elif(choice == '**'):
         exp = inp_1 ** inp_2
         print(exp)
         break
       else:
         print("Opps! Somthing went wrong : ( \n Please choose a valid operator. ")
         break
          

   elif(how_many_inputs == 3):
     inp_1 = int(input("Enter the first number: "))
     inp_2 = int(input("Enter the second number: "))
     inp_3 = int(input("Enter the third number:"))
     while(True):
       choice = str(input("Choose your operator \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Divission(/) \n :: "))
       if(choice == '+'):
         add = inp_1 + inp_2 + inp_3
         print(add)
         break
       elif(choice == '-'):
         sub = inp_1 - inp_2 - inp_3
         print(sub)
         break 
       elif(choice == '*'):
         mul = inp_1 * inp_2 * inp_3
         print(mul)
         break 
       elif(choice == '/'):
         div = inp_1 / inp_2 / inp_3
         print(div)
         break 
       else:
         print("Opps! Somthing went wrong : ( \n Please choose a valid operator. ")
         break
   elif(how_many_inputs == 4):
     inp_1 = int(input("Enter the first number: "))
     inp_2 = int(input("Enter the second number: "))
     inp_3 = int(input("Enter the third number:"))
     inp_4 = int(input("Enter the fourth number: "))
     while(True):
       choice = str(input("Choose your operator \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Divission(/) \n :: "))
       if(choice == '+'):
         add = inp_1 + inp_2 + inp_3 + inp_4
         print(add)
         break 
       elif(choice == '-'):
         sub = inp_1 - inp_2 - inp_3 - inp_4
         print(sub)
         break
       elif(choice == '*'):
         mul = inp_1 * inp_2 * inp_3 * inp_4
         print(mul)
         break
       elif(choice == '/'):
         div = inp_1 / inp_2 / inp_3 / inp_4
         print(div)
       else:
         print("Opps! Somthing went wrong : ( \n Please choose a valid operator. ")
         break
   elif(how_many_inputs == 5):
     inp_1 = int(input("Enter the first number: "))
     inp_2 = int(input("Enter the second number: "))
     inp_3 = int(input("Enter the third number:"))
     inp_4 = int(input("Enter the fourth number: "))
     inp_5 = int(input("Enter the fifth number: "))
     while(True):
       choice = str(input("Choose your operator \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Divission(/) \n :: "))
       if(choice == '+'):
         add = inp_1 + inp_2 +inp_3 + inp_4 + inp_5
         print(add)
         break
       elif(choice == '-'):
         sub = inp_1 - inp_2 - inp_3 - inp_4 - inp_5
         print(sub)
         break
       elif(choice == '*'):
         mul = inp_1 * inp_2 * inp_3 * inp_4 * inp_5
         print(mul)
         break 
       elif(choice == '/'):
         div = inp_1 / inp_2 / inp_3 / inp_4 / inp_5
         print(div)
         break 
       else:
         print("Opps! Somthing went wrong : ( \n Please choose a valid operator. ")
         break
   elif(how_many_inputs == 6):
     inp_1 = int(input("Enter the first number: "))
     inp_2 = int(input("Enter the second number: "))
     inp_3 = int(input("Enter the third number:"))
     inp_4 = int(input("Enter the fourth number: "))
     inp_5 = int(input("Enter the fifth number: "))
     inp_6 = int(input("Enter the sixth number: "))
     while(True):
       choice = str(input("Choose your operator \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Divission(/) \n :: "))
       if(choice == '+'):
         add = inp_1 + inp_2 +inp_3 + inp_4 + inp_5 + inp_6
         print(add)
         break
       elif(choice == '-'):
         sub = inp_1 - inp_2 - inp_3 - inp_4 - inp_5 - inp_6
         print(sub)
         break
       elif(choice == '*'):
         mul = inp_1 * inp_2 * inp_3 * inp_4 * inp_5 * inp_6
         print(mul)
         break
       elif(choice == '/'):
         div = inp_1 / inp_2 / inp_3 / inp_4 / inp_5 / inp_6
         print(div)
         break
       else:
         print("Opps! Somthing went wrong : ( \n Please choose a valid operator. ")
         break
   else:
     print("Error! please enter a number.")






     

