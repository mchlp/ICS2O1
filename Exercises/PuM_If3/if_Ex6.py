
#Michael Pu
#2016/10/12
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises C - 6

#Input
mark = int(input("Enter your mark: "))
#Calculations
if mark >= 80 and mark <= 100:
    lvl = "4"
elif mark >= 70 and mark < 80:
    lvl = "3"
elif mark >= 60 and mark < 70:
    lvl = "2"
elif mark >= 50 and mark < 60:
    lvl = "1"
elif mark < 50 and mark >= 0:
    lvl = ""
else:
    print ("Invalid Mark")
if mark <= 100 and mark >= 0:
    text = "level " + lvl
    if mark < 50:
        text = "R"
    print ("Student gets a '" + text + "'")
    
#Output
