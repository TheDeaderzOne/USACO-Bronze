import sys
inputs = sys.stdin.readline
outputs = sys.stdout.write
stalls = inputs().replace("\n","")
horseheight = sorted([int(x) for x in inputs().replace("\n","").split()],reverse=True)
stallheight = sorted([int(x) for x in inputs().replace("\n","").split()],reverse=True)
infolist = []
tempvar = 0
for x in range(len(horseheight)):
    for z in range(len(stallheight)):
        if horseheight[x]<=stallheight[z]:
            tempvar+=1
        else:
            break
    infolist.append(int(tempvar))
    tempvar = 0
def perms(info):
    perm = 1
    for z in range(len(info)):
        perm = (info[z]-z)*perm
    return perm
outputs(str(perms(infolist))+"\n")