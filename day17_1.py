from heapq import heappop,heappush
import sys
sys.setrecursionlimit(10000000)

s=open('day17.in').read().splitlines()
s=[[int(c) for c in l] for l in s]
n=len(s)
m=len(s[0])

# right, up, left, down
DIR=[(0,1), (-1,0), (0,-1), (1,0)]

v=set()
# (h,d,s,i,j)
q:list=[(0,1,1,0,0)]

h=0
while q:
    # if len(v)%100==0:print(len(v))
    h,d,t,i,j=heappop(q)
    # print(h,d,t,i,j)
    if (d,t,i,j) in v:continue
    v.add((d,t,i,j))
    if (i,j)==(n-1,m-1):break
    for f in range(4):
        if h>0 and (d-f+4)%4==2:continue
        x,y=i+DIR[f][0],j+DIR[f][1]
        if x<0 or y<0 or x>=n or y>=m:continue
        if d==f:
            if t<=1:continue
            ns=t-1
        else:ns=3
        heappush(q,(h+s[x][y],f,ns,x,y))

print(h)
