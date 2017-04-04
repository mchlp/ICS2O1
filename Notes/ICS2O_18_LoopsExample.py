import math


num = 1

print("number","\t","num**3","\t","root of num")
total=0
sumn3=0
while num <=10:

    total=total+num
    sumn3=sumn3+num**3
    print(num, "\t", num**3,"\t\t",round(math.sqrt(num),2))
    num = num + 1
print("\n\n",total,"\t",sumn3, sep="")	


low=int(input("Enter a lower number"))
hi=int(input("Enter a higher number"))
num=low
print("number","\t","num**3","\t","root of num")
total=0
sumn3=0
while num <=hi:

    total=total+num
    sumn3=sumn3+num**3
    print(num, "\t", num**3,"\t\t",round(math.sqrt(num),2))
    num = num + 1
print("\n\n",total,"\t",sumn3, "\n\n\n",sep="")	

    
