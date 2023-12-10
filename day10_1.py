from collections import defaultdict


s=list(filter(None,open('day10.in').read().splitlines()))

# (x,y) =>[(x,y),...]
con = defaultdict(list)

st=0,0
for i in range(len(s)):
    for j in range(len(s[i])):
        c=s[i][j]
        if c in '|LJ':
            con[i,j].append((i-1,j))
        if c in '-J7':
            con[i,j].append((i,j-1))
        if c in '|7F':
            con[i,j].append((i+1,j))
        if c in '-LF':
            con[i,j].append((i,j+1))
        if c == 'S':
            st=i,j

for n,m in [(-1,0),(0,1),(0,-1),(1,0)]:
    if st in con[st[0]+n,st[1]+m]:
        con[st].append((st[0]+n,st[1]+m))

lc=st
ls=-1,-1
sz=0
while not sz or lc!=st:
    print(lc)
    nx=con[lc][1] if con[lc][0] ==ls else con[lc][0]
    ls=lc
    lc=nx
    sz+=1
print(sz/2)
