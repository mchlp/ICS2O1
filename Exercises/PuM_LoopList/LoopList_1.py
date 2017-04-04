
#Michael Pu
#2016/11/21
#ICS2O1
#Ms.Strelkovska
#Looping Through Lists Exercises 1 

#Get User Input
listInputs = []
for i in ["first", "second"]:
    print("Enter the items for the %s list. Seperate list items with a comma (,)." %i)
    listInputs.append(input())

#Seperate Input Into Lists
lists = []
for stringList in listInputs:
    tempList = stringList.split(",")
    #Take Out Trailing or Leading Whitespace 
    for item in tempList:
        tempList[tempList.index(item)] = item.strip(" ")
    lists.append(tempList)

match = False
for listItem in lists[0]:
    if listItem in lists[1]:
        match = True
        break

print(match)
