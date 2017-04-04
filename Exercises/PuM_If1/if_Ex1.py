
#Michael Pu
#2016/10/03
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises A - 1

#Input & Check 1
validInput = False

while validInput == False:
    seniorInput = input("Are you a senior [yes/y/no/n]? ")
    senior = seniorInput.lower()
    if (senior == "yes" or senior == "y"):
        tax = 0.05
        people = " for seniors"
        validInput = True
    elif (senior == "no" or senior == "n"):
        tax = 0.13
        people = ""
        validInput = True
    else:
        print ("---------------------------------")
        print (seniorInput, "is not valid input. Accepted answers are: yes/y/no/n")

#Input 2
while True:
    try:
        costInput = input("\nWhat is the cost of your meal(>0)? ")
        cost = float(costInput)
        if cost <= 0:
            raise ValueError()    
        break
    except ValueError:
        print ("---------------------------------")
        print (costInput, "is not valid cost. \n"\
               "Enter a positive decimal without the dollar sign.")
    

#Calculations 2     
taxCost = tax * cost
total = taxCost + cost

#Output
print ("----------------------------------------------------------")
print ("%-30s %20.2f" %("The cost of your meal", cost))
print ("%-30s %20.2f" %("Plus " + str(int(tax*100)) + "% HST" + people, taxCost))
print ("%-30s %20s" %(" ", "------"))
print ("%-30s %20.2f" %("Total", total))
input()
