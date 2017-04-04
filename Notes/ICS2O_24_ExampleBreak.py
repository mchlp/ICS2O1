## This application asks for the number of students
## and asks for the mark that number of times. Then it
## displays the average.

numSt=int(input("How many students?"))
sumOfMarks=0
for st in range(1,numSt+1):

    m=float(input("Enter a mark for student"+str(st)))
    sumOfMarks+=m
average=sumOfMarks/numSt
print("average",average)

## Output
## How many students? 3
## Enter a mark for student 1 80
## Enter a mark for student 2 90
## Enter a mark for student 3 95
## average 88.33333333333333

#---------------------------------------------------------
## This application asks for the students'
## mark till -1 is entered. Then it
## displays the average.
st=0
sumOfMarks=0
while True:
    m=float(input("Enter a mark for student "+str(st+1)+" or -1 to exit  "))
    if m==-1:
        break
    sumOfMarks+=m
    st+=1
average=sumOfMarks/st
print("average",average)
## Output:
## Enter a mark for student 1 or -1 to exit  90
## Enter a mark for student 2 or -1 to exit  80
## Enter a mark for student 3 or -1 to exit  82
## Enter a mark for student 4 or -1 to exit  -1
## average 84.0
