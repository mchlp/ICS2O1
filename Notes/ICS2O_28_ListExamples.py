marks = []
m = input("Please, enter a mark or ! to exit")
while m != '!':
       marks.append(int(m))
       m = input("Please, enter a mark or ! to exit")
print(marks)
print("""\nWhat would you like to do
    1) Print average
    2) Print the lowest mark
    3) Print the highest mark
    4) Print all the marks in original order\n
    Select 1, 2, 3 or 4. 
    """)
choice=input()          # read input - user choice
while(choice=='1' or choice=='2' or choice=='3' or choice=='4'):
       print()                 # for a new line
       if choice == '1':
              total=0
              for x in marks:
                     total=total+x
              average=total/len(marks)
              print("Average:",average)
       elif choice == '2':
              low=marks[0]
              for x in marks:
                     if x<low:
                            low=x
              print("The lowerst marks is", low)
       elif choice == '3':
              hi=marks[0]
              for x in marks:
                     if x>hi:
                            hi=x
              print("The Highest marks is", hi)
       elif choice == '4':
              print("The entered marks are:")
              for x in marks:
                     print(x, end="  ")
       print("\n------------------------")
       print("""\nWhat would you like to do
          1) Print average
          2) Print the lowest mark
          3) Print the highest mark
          4) Print all the marks in original order\n
          Select 1, 2, 3 or 4. 
          """)
       choice=input()          # read input - user choice

print("Bye")                     
