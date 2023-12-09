lines = open('day3.in').read().splitlines()

n=len(lines)
m=len(lines[0])

ans = 0

def fs(i,j):
    while j>=0 and lines[i][j].isdigit():
        j-=1
    return j+1

def fe(i,j):
    while j<len(lines[i]) and lines[i][j].isdigit():
        j+=1
    return j

def fr(i,j):
    s,e = fs(i,j), fe(i,j)
    if s<e:
        return s,e

for i in range(n):
    line = lines[i]
    for j in range(m):
        if line[j]!='*': continue
        d=0
        ls=set()
        for x in range(-1, 2):
            for y in range(-1,2):
                ni,nj = i+x,j+y
                f=fr(ni,nj)
                if f:
                    ls.add((ni, *f))
        if len(ls)!=2: continue
        val=1
        for h,s,e in ls: val *=int(lines[h][s:e])
        print(i,j,ls,val)
        ans += val

print(ans)
