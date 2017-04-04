a="Hello There"
print(a)
a=a.lower()
print(a)
a=a.upper()
print(a)
word1=a[:5]
word1=word1.upper()
print("word1",word1)
word2=a[6:]
word2=word2.lower()
print("word2",word2)


a=input("enter something")
space=a.find(" ")
word1=a[:space]
word1=word1.upper()
print("word1",word1)
word2=a[space+1:]
word2=word2.lower()
print("word2",word2)
