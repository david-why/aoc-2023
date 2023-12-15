s=open('day13.in').read().splitlines()

def solve(mat:list[str]):
    n=len(mat)
    m=len(mat[0])
    for i in range(1,n):
        ok=2
        for k in range(min(i,n-i)):
            ok-=sum(mat[i-k-1][j]!=mat[i+k][j] for j in range(m))
            if ok<=0:break
        if ok==1:
            return 100*i
    for j in range(1,m):
        ok=2
        for k in range(min(j,m-j)):
            for i in range(n):
                if mat[i][j-k-1]!=mat[i][j+k]:
                    ok-=1
                    if not ok:break
            if not ok:break
        if ok==1:return j
    return 0

mat=[]
i=0
ans=0
while i<len(s):
    l=s[i]
    if not l and mat:
        ans+=solve(mat)
        mat=[]
    else:
        mat.append(l)
    i+=1
if mat:
    ans+=solve(mat)

print(ans)
