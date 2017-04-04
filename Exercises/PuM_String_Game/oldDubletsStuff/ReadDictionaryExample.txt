import random
english_words=""
with open("Eng_dictionary.txt") as word_file:
   for word in word_file:
        english_words += word
#print(english_words)
wordList=english_words.split("\n")
print(wordList)
print(random.choice(wordList))
print("ham" in english_words)
