import sys
inputee = sys.stdin.readline
outputee = sys.stdout.write
totaliters = 1
alphabet = list(inputee().replace("\n", ""))
word = list(inputee().replace("\n", ""))
wordlettercounter = [int(alphabet.index(x)+1) for x in word]
for xyz in range(1,len(wordlettercounter)):
    if wordlettercounter[xyz]<=wordlettercounter[xyz-1]:
        totaliters+=1
outputee(str(totaliters)+"\n")