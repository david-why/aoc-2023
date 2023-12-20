s=open('day16.in').read().splitlines()

# right, up, left, down
DIR=[(0,1), (-1,0), (0,-1), (1,0)]

n=len(s)
m=len(s[0])

en=[[0 for j in range(m)] for i in range(n)]

vis=set()
q:list[tuple[int,int,int]]=[(0,0,0)]

# TODO no hack
q[0]=(0,0,3)

while q:
    i,j,d=q.pop()
    print(i,j,d)
    if (i,j,d) in vis:continue
    vis.add((i,j,d))
    en[i][j]=1
    i+=DIR[d][0]
    j+=DIR[d][1]
    if i>=0 and i<n and j>=0 and j<m:
        c=s[i][j]
        # print(c)
        if c=='.':
            q.append((i,j,d))
        if c=='/':
            d={0:1,1:0,2:3,3:2}[d]
            q.append((i,j,d))
        if c=='\\':
            d={0:3,1:2,2:1,3:0}[d]
            q.append((i,j,d))
        if c=='|':
            if d in [0,2]:
                q.append((i,j,1))
                q.append((i,j,3))
            else:
                q.append((i,j,d))
        if c=='-':
            if d in [1,3]:
                q.append((i,j,0))
                q.append((i,j,2))
            else:
                q.append((i,j,d))

print(sum(sum(x) for x in en))
