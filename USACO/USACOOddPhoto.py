import sys

input = sys.stdin.readline
output = sys.stdout.write

numterms = int(input().replace("\n",""))
stringphotolist = input().replace("\n","").split()
photolist = [int(x) for x in stringphotolist]
modlist = sorted([x%2 for x in photolist])
modlistcounterfixed = len(modlist)
evens = 0

while 0 in modlist:
    modlist.pop(0)
    evens+=1

odds = modlistcounterfixed-evens

def maxdetec(even, odd):
    bruz = 0
    if even == odd or even == odd+1:
        maxnums = even+odd
        return maxnums
    else:
        if even>odd:
            if odd !=0:
                for _ in range(odd):
                    even-=1
                    if even == odd or even == odd+1:
                        maxnums = even+odd
                        return maxnums
            while even >= odd+2:
                even-=1
            maxnums = even+odd
            return maxnums
                
        elif odd>even:
            while bruz == 0:
                odd -= 2
                even +=1
                if odd <= even:
                    bruz=1

            if even == odd or even == odd+1:
                maxnums = even+odd
                return maxnums

            if even>odd:
                if odd !=0:
                    for _ in range(odd):
                        even-=1
                        if even == odd or even == odd+1:
                            maxnums = even+odd
                            return maxnums
                while even >= odd+2:
                    even-=1
                maxnums = even+odd
                return maxnums
                
output(str(maxdetec(evens,odds))+"\n")