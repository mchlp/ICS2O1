#Michael Pu
#Practice Test 1
#2016/10/17
import random

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
password = int(input("Enter your password: "))

if password != 123:
    print ("\nSorry, incorrect password.")

else:
    acNum = random.randint(1, 1000)
    acBal = random.randint(-50, 1000)
    numTran = random.randint(0, 15)
    
    if numTran > 0:
        if acBal < 0:
            acStat = "Negative Balance"
        else:
            acStat = "Positive Balance"
    else:
        acStat = "Inactive"
    intrst = abs(acBal)*((1+0.035/4)**(5*4))-abs(acBal)
    print("\n*****Account Info***********")
    print("Last name: " + lastName)
    print("First name: " + firstName)
    print("Account number: " + str(acNum))
    print("Balance: " + str(acBal))
    print("Number of last month transactions: " + str(numTran))
    print("Account Status: " + acStat)
    print("********************")
    print("If you will invest $%i for 5 years, you will earn $%.2f of interest." %(abs(acBal),intrst))

print("\nBye.")
    
