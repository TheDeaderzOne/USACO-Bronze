import sys

input = sys.stdin.readline
output = sys.stdout.write

NCows = int(input().replace("\n",""))

CowTypeList = list(input().replace("\n",""))

UpToAndIncludingRange = [int(e)-1 for e in input().replace("\n","").split()]

CowTypeListReverse = list(CowTypeList)
CowTypeListReverse.reverse()

ContainsAllHstart = 0
endH=0
ContainsAllGstart = 0
endG=0
for Hol in range(len(CowTypeList)):
    if CowTypeList[Hol]=='H':
        ContainsAllHstart = int(Hol)
        break

for Gu in range(len(CowTypeList)):
    if CowTypeList[Gu]=='G':
        ContainsAllGstart = int(Gu)
        break

for io in range(len(CowTypeList)):
    if CowTypeListReverse[io]=='G':
        endG = len(CowTypeList)-1-int(io)
        break

for uk in range(len(CowTypeList)):
    if CowTypeListReverse[uk]=='H':
        endH = len(CowTypeList)-1-int(uk)
        break

num = 0

if endG<=UpToAndIncludingRange[ContainsAllGstart] and endH<=UpToAndIncludingRange[ContainsAllHstart]:
    num+=1

for finals in range(max(ContainsAllGstart,ContainsAllHstart)):
    final = max(ContainsAllGstart,ContainsAllHstart)-finals-1
    if CowTypeList[final]!=CowTypeList[ContainsAllGstart]:
        if UpToAndIncludingRange[final]>=ContainsAllGstart:
            num+=1
    else:
        if UpToAndIncludingRange[final]>=ContainsAllHstart:
            num+=1

print(num)