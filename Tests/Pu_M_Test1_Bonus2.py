#Programming Test 1 - Bonus 2
#2016/10/18
#ICS2O1
#Michael Pu

#SEMI-PRIME PROBLEM
num = int(input("Enter an integer between 1 and 1000 inclusive: "))

prime = [2,]

for checkNum in range(2, num):
    ynPrime = True
    for a in prime:
        if checkNum%a == 0:
            ynPrime = False
    if ynPrime == True:
        prime.append(checkNum)

for i in prime:
    ynSemiPrime = False
    if num%i == 0:
        if ((num//i) in prime) == True:
            ynSemiPrime = True
        break

print (prime)

if ynSemiPrime == True:
    print("semiprime")
else:
    print("not")
        
        
