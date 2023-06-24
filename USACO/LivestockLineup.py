import time as tmr 
import copy as cpy
import math as math
time1 = tmr.time()
openee = open("lineup.in", "r")
outer = open("lineup.out", "w")
coworder = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
coworder.sort()

exdee = openee.readlines()
randomvar = 0
restraintnum = 0
restrictlist = []
for tel in exdee:
    xd = tel.replace("\n", "")
    if randomvar == 1:
        noo = xd.split(" must be milked beside ")
        restrictlist.append(noo)

    if randomvar == 0:
        restraintnum = int(xd)
        randomvar+=1
newlist = []
print (str(restrictlist) + " is restrict list")
for lister in range(restraintnum):
    if lister == 0:
        newlist.append(restrictlist[0])
    elif lister != 0:
        print(str(lister) + " is lister")
        for x in range (len(newlist)):

            if restrictlist[lister][0] in newlist[x]:
                xy = restrictlist[lister][1]
                
                if newlist[x].index(restrictlist[lister][0]) == 0:
                    newlist[x].insert(0, xy)
                    if newlist[x].count(restrictlist[lister][1]) == 2:
                        newlist[x].pop(0)

                elif newlist[x].index(restrictlist[lister][0]) == len(newlist[x])-1: 
                    newlist[x].append(xy)
                    if newlist[x].count(restrictlist[lister][1]) == 2:
                        newlist[x].pop()

                
            elif restrictlist[lister][1] in newlist[x]:
                ab = restrictlist[lister][0]
                if newlist[x].index(restrictlist[lister][1]) == 0:
                    newlist[x].insert(0, ab)
                    if newlist[x].count(restrictlist[lister][0]) == 2:
                        newlist[x].pop(0)

                elif newlist[x].index(restrictlist[lister][1]) == len(newlist[x])-1: 
                    newlist[x].append(ab)
                    if newlist[x].count(restrictlist[lister][0]) == 2:
                        newlist[x].pop()
            else:
                if x == len(newlist) - 1:
                    newlist.append(restrictlist[lister])
        print(newlist)

xlist = list(newlist)
tud = len(newlist)
for num in range (len(newlist)):
    tud = len(newlist)
    if num <= tud-1:
        firstset = set(newlist[num])
        for num2 in range(tud):
            if num2 <= tud-1:
                if num2 != num:
                    print (str(num2) + " is num2")
                    secondset = set(newlist[num2])
                    if secondset == firstset: 
                        newlist.remove(newlist[num2])

                    elif secondset.issubset(firstset):
                        newlist.remove(newlist[num2])

                    elif firstset.issubset(secondset):
                        newlist.remove(newlist[num])

                    tud = len(newlist)

                    print(str(tud) + " is tud")
                    
print(newlist)

thud = []
for tew in range(len(newlist)):
    if tew == 0:
        cons = cpy.deepcopy(newlist)
        cons2 = cpy.deepcopy(newlist)
    print (str(tew) + " is tew")
    for wet in range(len(newlist)):
        print(str(wet) + " is wet")
        if wet != tew:
            trex = 0
            for elementx in newlist[wet]:
                if elementx in newlist[tew]:
                    trex += 1
                    print (str(trex) + " is trex")
            if trex!=0:
                for elemen in newlist[tew]:
                    if elemen in newlist[wet]:
                        thud.append(elemen)
                

                print (str(thud) + " is def not a set")
                placee = [wet,tew]
                for lengthy in range (len(thud)):
                    if lengthy == 0:
                        indexvar = newlist[tew].index(thud[0])
                
                print (str(indexvar) + " is the indexvar")
                print (str(newlist[tew][len(thud)]) + str(newlist[wet][len(newlist[wet])-1]))
                if indexvar == 0 and newlist[tew] != [] and newlist[tew][1] == newlist[wet][len(newlist[wet])-1]:
                    print ("mark1")
                    xtd = newlist[wet]
                    xtd.reverse()
                    for bu in range (len(newlist[wet])-len(thud)):
                        newlist[tew].insert(0, xtd[len(thud)])
                        newlist[wet].remove((xtd[len(thud)]))

                elif indexvar == 0 and newlist[tew] != [] and newlist[tew][0] == newlist[wet][len(thud)-1]:
                    print ("mark2")
                    for yu in range (len(newlist[wet])-len(thud)):
                        newlist[tew].insert(0, newlist[wet][len(thud)])
                        newlist[wet].remove((newlist[wet][len(thud)]))

                elif indexvar != 0 and newlist[tew] != [] and newlist[tew][len(newlist[tew])-len(thud)] == newlist[wet][len(newlist[wet])-1]: 
                    print ("mark3")
                    xtd = newlist[wet]
                    xtd.reverse()
                    print(str(xtd) + " is xtd")
                    for cu in range (len(newlist[wet])-len(thud)):
                        newlist[tew].append(xtd[len(thud)])
                        newlist[wet].remove((xtd[len(thud)]))

                elif indexvar != 0 and newlist[tew] != [] and newlist[tew][len(newlist[tew])-len(thud)] == newlist[wet][0]:
                   print ("mark4")
                   for su in range (len(newlist[wet])-len(thud)):
                        newlist[tew].append(newlist[wet][len(thud)])
                        newlist[wet].remove((newlist[wet][len(thud)]))
                
                newlist[wet] = []
                print(str(newlist) + " is the answer yes no")
                thud.clear()

print(str(newlist) + " is the list x")

oglist = []  

newlistcop = cpy.deepcopy(newlist)
for xiwa in range(len(newlist)):
    print(xiwa)
    print(newlist)
    if newlist[xiwa] == []:
        newlistcop.remove(newlist[xiwa])

newlist = newlistcop

print(newlist)
  
for x in range(len(newlist)):
    old = list(newlist[x])
    old.reverse()
    holder = list(old)
    old.reverse()
    g = [old[0], holder[0]]
    g.sort()
    if g[0] == old[0]:
        oglist.append(old)
    if g[0] == holder[0]:
        oglist.append(holder)

print(oglist)

for t in range (len(newlist)):
    for f in range(len(newlist[t])):
        coworder.remove(newlist[t][f])
for e in range(len(coworder)):
    coworder[e] = [coworder[e]]
streedle = ""

print(str(oglist) + "is og")

for yutu in range(len(oglist)):
    coworder.append(oglist[yutu])

coworder.sort()

print (coworder)

time2 = tmr.time()

for xf in range(len(coworder)):
    print (xf)
    for xs in range(len(coworder[xf])):
        outer.writelines(str(coworder[xf][xs]) + "\n")

print(time2-time1)