print("Please enter your name")
name=input()
#get a first letter of a name
first_Letter=name[0]
first_Letter=first_Letter.upper()

#index of space
space_index=name.find(" ")

#get a second letter of a name
second_Letter=name[space_index+1]
second_Letter=second_Letter.upper()

# output
print(first_Letter+"."+second_Letter+".")
