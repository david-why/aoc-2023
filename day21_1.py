s=open('day21.in').read().splitlines()
n=len(s)
m=len(s[0])

# right, up, left, down
DIR=[(0,1), (-1,0), (0,-1), (1,0)]

p0=(0,0)
for i in range(n):
    for j in range(m):
        if s[i][j]=='S':
            p0=i,j
            break

q=[p0]
for _ in range(64):
    # print(_,len(q),q)
    ad=set()
    for _ in range(len(q)):
        i,j =q.pop(0)
        for d in range(4):
            x,y=i+DIR[d][0],j+DIR[d][1]
            if x>=0 and x<n and y>=0 and y<m and s[x][y]!='#' and (x,y) not in ad:
                q.append((x,y))
                ad.add((x,y))

print(len(ad))
