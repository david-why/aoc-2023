s=open('day13.in').read().splitlines()

def solve(mat:list[str]):
    n=len(mat)
    m=len(mat[0])
    for i in range(1,n):
        ok=1
        for k in range(min(i,n-i)):
            if mat[i-k-1]!=mat[i+k]:
                ok=0
                break
        if ok:
            return 100*i
    for j in range(1,m):
        ok=1
        for k in range(min(j,m-j)):
            for i in range(n):
                if mat[i][j-k-1]!=mat[i][j+k]:
                    ok=0;break
            if not ok:break
        if ok:return j
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
