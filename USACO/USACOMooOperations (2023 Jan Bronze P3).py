import sys
import math

input = sys.stdin.readline
output = sys.stdout.write

StringNum = int(input().replace("\n",""))

StringList = []

for _ in range(StringNum):
    StringList.append(list(input().replace("\n","")))

def MooOperator(StrList):
    Pops = len(StrList)-3
    MinSteps=math.inf
    for xy in range(len(StrList)-2):
        x=StrList[xy:3+xy]
        if x[1] == 'M':
            pass
        elif x[0]=='M' and x[2]=='O':
            MinSteps = 0
            return Pops
        elif x[0]=='O' and x[2]=='M':
            MinSteps = min(MinSteps,2)
        elif x[0]=='O' and x[2]=='O':
            MinSteps = min(MinSteps,1)
        elif x[0]=='M' and x[2]=='M':
            MinSteps = min(MinSteps,1)
    if MinSteps == math.inf:
        return -1
    return Pops+MinSteps

for x in StringList:
    output(str(MooOperator(x))+"\n")