from collections import Counter

s=[x.split() for x in open('day7.in').read().splitlines()]
s=list(filter(None, s))

def mp(c):
    t=[]
    for x in c:
        t.append('23456789TJQKA'.index(x))
    return tuple(t)

def od(c):
    c=c[0]
    d=len(set(c))
    z=mp(c)
    if d==1:
        return (10,z)
    if d==2:
        x=Counter(c)
        if max(x.values())==4:
            return 9,z
        return (8,z)
    if d==3:
        x=Counter(c)
        if max(x.values())==3:
            return 7,z
        return 6,z
    if d==4:
        return 5,z
    return 4,z

s.sort(key=od)
ans=0
cnt=1
for _,b in s:
    b=int(b)
    ans+=cnt*b
    cnt+=1
    
print(ans)
