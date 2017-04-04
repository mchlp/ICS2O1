#Programming Test 2
#2016/11/30
#Michael Pu

import string

numLines = int(input("How many lines? "))

for line in range(numLines):
    code = []
    encode = (input("Enter a code: ")).strip(" ")
    i = 0
    decode = ""
    curNum = ""
    curSym = ""
    while i < len(encode):
        if (encode[i] in (string.digits)):
            curNum += encode[i]
        else:
            curSym = encode[i]
            curNum = int(curNum)
            decode += curSym*curNum
            curNum = ""
        i+=1
    print(decode)
            
        
