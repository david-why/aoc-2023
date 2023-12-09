t=open('day4.in').read().splitlines()

mul={i:1 for i in range(1,len(t)+1)}

def mt(s):
    _,_,s=s.partition(':')
    s=s.strip()
    a,b=s.split(' | ')
    a=list(map(int, a.split()))
    b=list(map(int, b.split()))
    v= len(set(a).intersection(b))
    return v

for i in range(1,len(t)+1):
    card=t[i-1]
    m=mt(card)
    for k in range(m):
        j=i+1+k
        if j>len(t): break
        mul[j]+=mul[i]

print(sum(mul.values()))
