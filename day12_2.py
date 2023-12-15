s=open('day12.in').read().splitlines()

cc={}

def dfs(s:str,pt:list[int],i:int,p:int):
    if (i,p) in cc:
        return cc[i,p]
    if p>=len(pt):
        return int(all(s[j]!='#' for j in range(i,len(s))))
    if i>=len(s):
        return 0
    # print(s,pt,i,p)
    num=pt[p]
    ans=0
    if i+num-1<len(s) and all(s[j]!='.' for j in range(i,i+num)) and (p==len(pt)-1 or i+num<len(s) and s[i+num]!='#'):
        ans+=dfs(s,pt,i+num+(p!=len(pt)-1),p+1)
    if s[i]!='#':
        ans+=dfs(s,pt,i+1,p)
    # print(ans)
    cc[i,p]=ans
    return ans

def solve(s:str):
    s,l = s.split()
    pt=l.split(',')
    pt=[int(p) for p in pt]
    # print(s,pt,dfs(s,pt,0,0))
    cc.clear()
    return dfs('?'.join(s for _ in range(5)),pt*5,0,0)

ans=0
for l in s:
    if l:
        ans+=solve(l)
print(ans)
