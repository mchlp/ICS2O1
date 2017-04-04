import random
row=4
col = 5
alf="abcdefg"
grid = [[random.choice(alf) for x in range(col)] for y in range(row)]
print(grid)
print("\n----------------------\n")  
for i in range(row):
    print(grid[i])

print("\n----------\n")    
for i in range(row):
    for j in range(col):
        print(grid[i][j], end="|")
    print("\n----------")    
grid[2][2]='x'
print("\n----------------------\n") 
for i in range(row):
    for j in range(col):
        print(grid[i][j], end="|")
    print("\n----------") 
