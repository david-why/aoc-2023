from collections import Counter

s=[x.split() for x in open('day7.in').read().splitlines()]
s=list(filter(None, s))

def mp(c):
    t=[]
    for x in c:
        t.append('J23456789TQKA'.index(x))
    return tuple(t)

def od(c):
    c=c[0]
    z=mp(c)
    q=c.count('J')
    c=c.replace('J', '')
    x=Counter(c)
    if len(x)==0:
        qq='A'
    else:
        qq=x.most_common()[0][0]
    c+=qq*q
    d=len(set(c))
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
