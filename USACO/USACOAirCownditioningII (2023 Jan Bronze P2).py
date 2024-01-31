import sys
from itertools import combinations
import time as tmr
input = sys.stdin.readline
output = sys.stdout.write

NCows, MAirCons = [int(x) for x in input().replace("\n","").split()]
CowDescriptions = []
for _ in range(NCows):
    CowDescriptions.append([int(x) for x in input().replace("\n","").split()])
Rooms = []
for op in range(len(CowDescriptions)):
    for iu in range(CowDescriptions[op][1]-CowDescriptions[op][0]+1):
        Rooms.append([CowDescriptions[op][0]+iu,CowDescriptions[op][2]])
AirConDescriptions = []
for _ in range(MAirCons):
    AirConDescriptions.append([int(x) for x in input().replace("\n","").split()])
CheckerList = []
Representation = []
for ind in range(len(AirConDescriptions)):
    Representation.append(ind)
ComboList = []
for x in range(2,len(AirConDescriptions)+1):
    l = list(combinations(Representation,x))
    for element in l:
        xut=list(element) 
        for _ in range(len(xut)):
            xut[_]=AirConDescriptions[xut[_]]
        ComboList.append(xut)
RoomsCovered=[0]*len(Rooms)
prices = []

def CheckFunc(inputcombo,emptylist,rooms):
    for p in range(len(inputcombo)):
        for o in range(len(rooms)):
            if inputcombo[p][0]<=rooms[o][0]<=inputcombo[p][1]:
                emptylist[o]+=inputcombo[p][2]
    for n in range(len(rooms)):
        if rooms[n][1]>emptylist[n]:
            return False
    intu = 0
    for p in range(len(inputcombo)):
        intu+=inputcombo[p][3]
    prices.append(intu)

for x in AirConDescriptions:
    RoomsCovered=[0]*len(Rooms)
    x = [x]
    CheckFunc(x,RoomsCovered,Rooms)

for r in ComboList:
    RoomsCovered=[0]*len(Rooms)
    CheckFunc(r,RoomsCovered,Rooms)

print(min(prices))