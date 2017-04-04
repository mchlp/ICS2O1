def getOneDigit(num):
    while num >= 10:
        strNum = str(num)
        total = 0
        for digit in strNum:
            total += int(digit)
        num = total
    return num

for i in range(5):
    numList = list(input().split())
    for num in numList:
        total = 0
        for j in range(len(num)-1, -1, -2):
            total += getOneDigit(int(num[j])*2)
        for j in range(len(num)-2, -1, -2):
            total += int(num[j])
        checkDigit = (10-(total%10))%10
        print(checkDigit, end="")
    print()
