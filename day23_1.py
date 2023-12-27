import sys
sys.setrecursionlimit(100000)

s=open('day23.in').read().splitlines()

SL='>^<v'
# right, up, left, down
DIR=[(0,1), (-1,0), (0,-1), (1,0)]

def dx(i,j):
    return 1<<(i*len(s[0])+j)

cc={}
ans =0

# vis=set()
vis=0
def dfs(i,j):
    global ans,vis
    # kk =(i,j,hash(frozenset(vis)))
    kk=(i,j,vis)
    if kk in cc:
        return cc[kk]
    if i<0 or j<0 or i>=len(s) or j>=len(s[0]):return 0
    if s[i][j]=='#':
        return 0
    ddd=dx(i,j)
    # if (i,j) in vis:
    if vis&ddd:
        return 0
    vis|=ddd
    # vis.add((i,j))
    val=0
    if s[i][j] in SL:
        d=SL.index(s[i][j])
        val=dfs(i+DIR[d][0],j+DIR[d][1])
    else:
        for d in range(4):
            val=max(val,dfs(i+DIR[d][0],j+DIR[d][1]))
    # vis.remove((i,j))
    vis&=~ddd
    cc[kk] = val+1
    return val+1

print(dfs(0,1)-1)
