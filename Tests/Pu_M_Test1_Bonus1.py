#Programming Test 1 - Bonus
#2016/10/18
#ICS2O1
#Michael Pu

#ROUND PROBLEM

num = input("Enter a number: ")
decPos = (num.find("."))
preRoundNum = num[:decPos+3]

checkDig = int(preRoundNum[-1])
checkDig = checkDig + 5
addDig = (checkDig//10)/10

roundNum = float(preRoundNum[:decPos+2])
roundNum = roundNum + addDig
roundNum = str(roundNum)

newDecPos = (roundNum.find("."))
newRoundNum = roundNum[:newDecPos+2]

print(newRoundNum)
