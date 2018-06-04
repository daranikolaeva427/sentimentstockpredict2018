import os
from function import funct_gen
from collections import Counter

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

i = 0
j = 0
wordlist = []
f = open("lemmatised.txt", encoding = 'utf-8')
for line in f:
    for item in funct_gen(line):
        word = item.string
        wordlist.append(BMP(word))
        i += 1
        if word[len(word)-1] == '?':
            j += 1

print(i)
print(j)

cntr = Counter(wordlist)
print(cntr)
