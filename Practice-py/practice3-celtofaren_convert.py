#Practice3;
#Celcius to fahernhite;
choice = int(input(" 1) Celcius to Fhrenhite ; 2) Fhrenhite to Celcius; Enter your choice:"))
if (choice == 1):
    cel = int(input("Enter your temp into Celcius: "))
    fhren = (cel+32)*9/5
    print("Converted the value into Fhrenhite,",fhren)
elif (choice == 2):
    fhren = int(input("Enter your temp into Fhrenhite: "))
    cel = (fhren-32)*5/9
    print("Convert into Celcius ,",cel)
else:
    print("Plese enter a positive number.")