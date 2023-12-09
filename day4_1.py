t=open('day4.in').read().splitlines()

ans=0
for s in t:
    _,_,s=s.partition(':')
    s=s.strip()
    a,b=s.split(' | ')
    a=list(map(int, a.split()))
    b=list(map(int, b.split()))
    v= len(set(a).intersection(b))
    if v:
        ans+=2**(v-1)

print(ans)
