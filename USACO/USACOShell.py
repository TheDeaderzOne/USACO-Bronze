import time as tmr
time1 = tmr.time()
openar = open("shell.in", "r")
openarw = open("shell.out", "w")
readerlines = openar.readlines()
gamepos = []
monte = [1,2,3]
sol1 = 1; sol2 = 2; sol3 = 3
solx1counter = 0; soly2counter = 0; solz3counter = 0
directions = []
guess = []
bex = 0
swapnum = 0
for x in readerlines:
    hed = x.replace("\n", "")
    if bex == 0:
        swapnum = int(x)
        bex+=1
    else:
        directions.append(hed.split(" "))

for x in range(swapnum):
    listified = list(directions[x])
    for x in range (3):
        listified[x] = int(listified[x])
    guess.append(listified[2])
    onepos = monte[listified[0]-1]
    twopos = monte[listified[1]-1]
    monte[listified[0]-1] = twopos
    monte[listified[1]-1] = onepos
    gamepos.append(list(monte))

for x in range(swapnum):
    if sol1 == gamepos[x][guess[x]-1]:
        solx1counter+=1
    if sol2 == gamepos[x][guess[x]-1]:
        soly2counter+=1
    if sol3 == gamepos[x][guess[x]-1]:
        solz3counter+=1

finalans = max(solx1counter,soly2counter,solz3counter)

for x in range(1):
    openarw.writelines(str(finalans))
time2 = tmr.time()
print(time2-time1)