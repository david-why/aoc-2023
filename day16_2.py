s=open('day16.in').read().splitlines()

# right, up, left, down
DIR=[(0,1), (-1,0), (0,-1), (1,0)]

n=len(s)
m=len(s[0])

en=[[0 for j in range(m)] for i in range(n)]

vis=set()
q:list[tuple[int,int,int]]=[]


def run(v=0):
    while q:
        i,j,d=q.pop()
        if v:print(i,j,d)
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
                    if v:print('yes',i,j,d)
                    q.append((i,j,0))
                    q.append((i,j,2))
                else:
                    q.append((i,j,d))

    return sum((sum(x) for x in en))


ans=0
for x in range(m):
    q.clear()
    vis.clear()
    en=[[0 for j in range(m)] for i in range(n)]
    c=s[0][x]
    if c=='-':
        q.append((0,x,0))
        q.append((0,x,2))
    else:
        q.append((0,x,{'\\':0,'/':2}.get(c,3)))
    # if x==3:print(run(1),*en,sep='\n')
    ans=max(ans,run())
    q.clear()
    vis.clear()
    en=[[0 for j in range(m)] for i in range(n)]
    c=s[-1][x]
    if c=='-':
        q.append((n-1,x,0))
        q.append((n-1,x,2))
    else:
        q.append((n-1,x,{'\\':2,'/':0}.get(c,1)))
    ans=max(ans,run())

for x in range(n):
    q.clear()
    vis.clear()
    en=[[0 for j in range(m)] for i in range(n)]
    c=s[x][0]
    if c=='|':
        q.append((x,0,1))
        q.append((x,0,3))
    else:
        q.append((x,0,{'\\':3,'/':1}.get(c,0)))
    ans=max(ans,run())
    q.clear()
    vis.clear()
    en=[[0 for j in range(m)] for i in range(n)]
    c=s[x][-1]
    if c=='|':
        q.append((x,m-1,3))
        q.append((x,m-1,1))
    else:
        q.append((x,m-1,{'\\':1,'/':3}.get(c,2)))
    ans=max(ans,run())


print(ans)
