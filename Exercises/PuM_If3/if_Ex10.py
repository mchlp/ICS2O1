
#Michael Pu
#2016/10/13
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises C - 10

#Input
validInput = False
while validInput == False:
    option = int(input('''
Choose one of the following:
1 - To convert pounds to kilograms
2 - To convert miles to kilometers
3 - To display conversion table
4 - Exit
    '''))
    if option == 1 or option == 2 or option == 3 or option == 4:
        validInput = True
    else:
        print (option, "is not valid input.")
#Calculations
    if option == 1:
        lb = float(input("Enter the number of pounds: "))
        kg = lb * 0.45359237
        print (lb, "pounds is equal to", kg, "kilograms")
    elif option == 2:
        mi = float(input("Enter the number of miles: "))
        km = mi * 1.609344
        print (mi, "miles is equal to", km, "kilometers")
    elif option == 3:
        print ('''
To convert	    | Into 		 | Multiply by 
--------------------|--------------------|---------------
square meters 	    | square centimeter  | 10000 
square meters       | square feet	 | 10.763911 
square kilometers   | square miles	 | 0.386109
''')
    elif option == 4:
        exit()
