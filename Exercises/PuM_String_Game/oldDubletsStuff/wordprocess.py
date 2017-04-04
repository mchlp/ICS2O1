# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:12:12 2016

@author: tiansopu
"""
import collections
import datetime

def readword(filename):
    words = set()
    with open(filename) as file:
        for line in file:
            word = line.strip().lower()
            if len(word)>1:
                words.add(word)
    return words

def findmatch(words):
    matchList = collections.OrderedDict()
    count = 0
    for word in words:
        #print("Count:", count, "Processing:", word);
        count +=1
        if (count % 1000 ==0):
            print(count)
        matchList[word]=collections.OrderedDict()
        matchList[word]["complex"]=[]
        matchList[word]["path"]=[]
        matchList[word]["complex"].append(set())
        matchList[word]["path"].append(dict())
        for index in range(0, len(word)):
            wordhead = word[0:index]
            wordtrail = word[index+1:]
            charorder = ord(word[index:index+1])
            for char in range(97, 123):
                if (char != charorder):
                    newword = wordhead + chr(char) + wordtrail
                    if (newword in words):
                        matchList[word]["complex"][0].add(newword)
                        matchList[word]["path"][0][newword] = [word]
                        #print("====find matched", word, "<=>", newword)
    return matchList    

def findComplexPath(matchList, words, complexity):
    if (complexity<2):
        return
    count = 0
    for word in words:
        count +=1
        if (count % 1000 ==0):
            print(count)        
        currcomplexity = 1
        #print("==============processing:", word)
        while(currcomplexity < complexity):
            matchList[word]["complex"].append(set())
            matchList[word]["path"].append(dict())
            for prevcomplexword in matchList[word]["complex"][currcomplexity-1]:
#                print("word:", word," prev:",prevcomplexword, 
#                      " match:",matchList[prevcomplexword]["complex"][0])
                for complexword in matchList[prevcomplexword]["complex"][0]:
                    complexwordinshortpath = False
                    if (complexword == word):
                        complexwordinshortpath = True

                    for prevcomplex in range(0, currcomplexity):
                        if (complexword in matchList[word]["complex"][prevcomplex]):
                            complexwordinshortpath = True

                    if (complexwordinshortpath==False):
                        matchList[word]["complex"][currcomplexity].add(complexword)
                        matchList[word]["path"][currcomplexity][complexword] = (matchList[word]["path"][currcomplexity-1][prevcomplexword]+[prevcomplexword])
                        #print("find complex", currcomplexity+1, 
                        #      " from ", word, " to prev ", prevcomplexword, 
                        #      " to ", complexword) 

            currcomplexity +=1

time1 = datetime.datetime.now()
wordList = readword("Eng_dictionary.txt")  
matchList = findmatch(wordList)
time2 = datetime.datetime.now()
findComplexPath(matchList, wordList, 2)
time3 = datetime.datetime.now()

print("T1", time1, "T2", time2, "T3", time3)
input()

print("complex 2============")
for word in wordList:
    for searchWord in matchList[word]["complex"][1]:
        if len(matchList[word]["complex"][1])>0:   
            print(word, "=>", searchWord)
            print(word, "PATH ->", matchList[word]["path"][1][searchWord])
    
