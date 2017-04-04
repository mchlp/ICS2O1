
#Michael Pu
#2016/09/16
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Exercise Set 3 - Ex 4

#Set Global Variables
dash = "-"
star = "*"
emptyLine = ""
name = "Michael Pu"
curClass = "ICS2O1"
school = "Don Mills Collegiate Institute"
period = "Period"
day1 = "Day 1"
day2 = "Day 2"
p0 = "HF"
p1 = "Period 1"
p2 = "Period 2"
lunch = "Lunch"
p3 = "Period 3"
p4 = "Period 4"
p0Time = "08:45-08:50"
p1Time = "08:50-10:05"
p2Time = "10:10-11:25"
lunchTime = "11:25-12:25"
p3Time = "12:30-13:45"
p4Time = "13:50-15:05"

#Declare Function to Print Header
def printHeader():
    print(emptyLine)
    print("%-13s %80s" %("Name:", name))
    print("%-13s %80s" %("Course:", curClass))
    print("%-13s %80s" %("School:", school))
    print(emptyLine)

#Declare Function to Print Classes
def printClasses(p, pTime, classCode1a, classCode2a, classCode1b, classCode2b, classTeach1a, classTeach2a, classTeach1b, classTeach2b, classRm1a, classRm2a, classRm1b, classRm2b):
    print("%-15s %-20s %-20s %-20s %-20s" %(p, classCode1a, classCode2a, classCode1b, classCode2b))
    print("%-15s %-20s %-20s %-20s %-20s" %(pTime, classTeach1a, classTeach2a, classTeach1b, classTeach2b))
    print("%-15s %-20s %-20s %-20s %-20s" %("", classRm1a, classRm2a, classRm1b, classRm2b))

#Declare Function to Print Semester
def printSemester(sem):
    print("----------------------------------------------------------------------------------------------")
    print("Semester", sem)
    print("----------------------------------------------------------------------------------------------")
    #Print First Row
    printClasses(period, dash, day1, day2, day1, day2, dash, dash, dash, dash, emptyLine, emptyLine, emptyLine, emptyLine)

    #Print Headings   
    printClasses(p0, p0Time, HF, HF, HF, HF, HFTeach, HFTeach, HFTeach, HFTeach, HFRm, HFRm, HFRm, HFRm)
    print(emptyLine)

    #Print Period 1   
    printClasses(p1, p1Time, pA, pA, pA, pA, pATeach, pATeach, pATeach, pATeach, pARm, pARm, pARm, pARm)
    print(emptyLine)

    #Print Period 2 
    printClasses(p2, p2Time, pB1, pD, pB2, pD, pB1Teach, pDTeach, pB2Teach, pDTeach, pB1Rm, pDRm, pB2Rm, pDRm)
    print(emptyLine)

    #Print Lunch
    printClasses(lunch, lunchTime, star, star, star, star, emptyLine, emptyLine, emptyLine, emptyLine, emptyLine, emptyLine, emptyLine, emptyLine)
    print(emptyLine)

    #Print Period 3 
    printClasses(p3, p3Time, pC, pC, pC, pC, pCTeach, pCTeach, pCTeach, pCTeach, pCRm, pCRm, pCRm, pCRm)
    print(emptyLine)

    #Print Period 4 
    printClasses(p4, p4Time, pD, pB1, pD, pB2, pDTeach, pB1Teach, pDTeach, pB2Teach, pDRm, pB1Rm, pDRm, pB2Rm)
    print(emptyLine)



#Print Header
printHeader()

#Semester 1 Variables
HF = "1-10F"
pA = "ENG2D6"
pB1 = "CHV2O1"
pB2 = "GLC2O1"
pC = "SNC2D6"
pD = "ICS2O1"
HFTeach = "MacInnis, A."
pATeach = "MacInnis, A."
pB1Teach = "Carter, D."
pB2Teach = "Whiteside, C."
pCTeach = "Kamen, J."
pDTeach = "Strelkovska, H."
HFRm = "130"
pARm = "130"
pB1Rm = "118"
pB2Rm = "226"
pCRm = "214"
pDRm = "118"

#Print Semester 1 Timetable
printSemester(1)

#Semester 2 Variables
HF = "2-10E"
pA = "TEJ2O1"
pB1 = "SBI3U6"
pB2 = "SBI3U6"
pC = "CHC2D6"
pD = "MPM2D6"
HFTeach = "Tam, J."
pATeach = "Tam, J."
pB1Teach = "McKinlay, M."
pB2Teach = "McKinlay, M."
pCTeach = "Greene, B."
pDTeach = "MacDonald, I."
HFRm = "118"
pARm = "118"
pB1Rm = "205"
pB2Rm = "205"
pCRm = "126"
pDRm = "202"

#Print Semester 2 Timetable
printSemester(2)

