
#Michael Pu
#2016/10/21
#ICS2O1
#Ms.Strelkovska
#Repetition Exercises A - 5

#Input
inputCorrect = False
while inputCorrect == False:
    lower = int(input("Enter the lower number: "))
    higher = int(input("Enter the higher number: "))
    print()
    if lower <= higher:
        inputCorrect = True
    else:
        print("The higher number is lower than the lower number.")

#Calculations
for num in range(lower,higher+1):
    if ((num-lower)//10 > 0) and ((num-lower)%10 == 0):
        print("-------------------------------------")
    print ("%6i%5s" %(num, chr(num)))
