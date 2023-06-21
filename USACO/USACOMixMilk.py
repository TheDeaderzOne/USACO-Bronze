openee = open("10.in", "r")
outputee = open("mixmilk.out", "w")
openeed = openee.readlines()
listlimit = []
listmilksamount = []
pours = 100
for x in openeed:
    brug = x.replace("\n", "")
    ne = brug.split(" ")
    listlimit.append(int(ne[0]))
    listmilksamount.append(int(ne[1]))

for x in range(pours):
    if x%3 == 0:
        if listmilksamount[0] + listmilksamount[1] <= listlimit[1]:
            placeholder = listmilksamount[0]
            listmilksamount[0] = 0
            listmilksamount[1] += placeholder
        if listmilksamount[0] + listmilksamount[1] > listlimit[1]:
            listmilksamount[0] = (listmilksamount[0] - listlimit[1])+listmilksamount[1]
            listmilksamount[1] = listlimit[1]

    if x%3 == 1:
        if listmilksamount[1] + listmilksamount[2] <= listlimit[2]:
            placeholder = listmilksamount[1]
            listmilksamount[1] = 0
            listmilksamount[2] += placeholder

        if listmilksamount[1] + listmilksamount[2] > listlimit[2]:
            listmilksamount[1] = (listmilksamount[1] - listlimit[2])+listmilksamount[2]
            listmilksamount[2] = listlimit[2]

    if x%3 == 2:
        if listmilksamount[2] + listmilksamount[0] <= listlimit[0]:
            placeholder = listmilksamount[2]
            listmilksamount[2] = 0
            listmilksamount[0] += placeholder
        if listmilksamount[2] + listmilksamount[0] > listlimit[0]:
            listmilksamount[2] = (listmilksamount[2] - listlimit[0])+listmilksamount[0]
            listmilksamount[0] = listlimit[0]


for x in range(len(listmilksamount)):
    outputee.writelines(str(listmilksamount[x]) + "\n")
