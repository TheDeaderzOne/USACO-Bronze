import time as tmr
import math as math 
time1 = tmr.time()
alphabetlist = [0] * 26
replaceralphabetlist = [0] * 26
alphabetliststr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blocker = open("blocks.out", "w")
# for x in range(26):
#     blocker.writelines("")
b = open("blocks.in", "r")
t = b.readlines()
termnumber = 0
words = []
trackeroflines = 1

for x in t:
    if "\n" in x:
        x = x.replace("\n","")
    h = x.split(" ")
    if trackeroflines == 1:
        termnumber = int(x)
    if trackeroflines != 1:
        words.append(h)
    trackeroflines+=1
possibilities = 2**termnumber
testlist = []
intstrlist = []
for x in range(possibilities):
    s = bin(x)
    if "0b" in s:
        s = s.replace("0b","")
    intstrlist.append(s)

testlist = [0] * len(words)
wordchecker1 = []
for x in range(possibilities):
    listmaker = list(intstrlist[x])
    while len(listmaker) < termnumber:
        listmaker.insert(0, "0")
    for l in range(termnumber):
        if listmaker[l] == "0":
            word = words[l][0]
        if listmaker[l] == "1":
            word = words[l][1]
        wordchecker1.append(word)
    
    for zed in range(len(wordchecker1)):
        for yeti in range (26):
            replaceralphabetlist[yeti] += wordchecker1[zed].count(alphabetliststr[yeti])
    for y in range(26):
        if replaceralphabetlist[y] > alphabetlist[y]:
            alphabetlist[y] = replaceralphabetlist[y]
    replaceralphabetlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    wordchecker1 = []


for x in range(26):
    blocker.writelines(str(alphabetlist[x])+"\n")

time2 = tmr.time()

print (str(time2-time1) + " seconds have elapsed")