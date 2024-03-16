#Match case in python
'''Match case is similar as switch case in othar programming languages.'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = str(input("Enter your choice you want: \n Addition(+) \n Substraction(-) \n Multiplication(*) \n Division(/) \n ::"))
match(choice):
     case '+':
          print("Addition:", a+b)
          
     case '-':
          print("Substraction:", a-b)

     case '*':
          print("Multiplication:", a*b)
     
     case '/':
          print("Division:", a/b)
     case _:
          print("Opps! somthing went wrong : ( \n Please chose a valid operator.")



