
#Michael Pu
#2016/10/19
#ICS2O1
#Ms.Strelkovska
#Repetition Exercises A - 1

#Input
top = int(input("What is the top mile in your conversion chart? "))

#Calculations
print("\n\t\t%s%s" %("Miles".center(5, " "), "Kilometers".center(15, " ")))
print("\t\t%s%s" %("-----".center(5, " "), "----------".center(15, " ")))

mile = 1
while mile <= top:
    km = mile*1.6093
    km = round(km, 2)
    strMile = str(mile)
    strKm = str(km)
    print("\t\t%s%s" %(strMile.center(5, " "), strKm.center(15, " ")))
    mile = mile + 1
