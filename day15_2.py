from collections import defaultdict

s=open('day15.in').read().replace('\n', '').split(',')

def h(s):
    a=0
    for c in s:
        a=(a+ord(c))*17%256
    return a

bxs=defaultdict(list)

for x in s:
    hh=h(x.split('=')[0].strip('-'))
    if '=' in x:
        nm,le =x.split('=')
        for i,k in enumerate(bxs[hh]):
            if k[0]==nm:
                bxs[hh][i] = (nm,int(le))
                break
        else:
            bxs[hh].append((nm,int(le)))
    elif '-' in x:
        x=x[:-1]
        for k in bxs[hh]:
            if k[0]==x:
                bxs[hh].remove(k)
                break

a=0
for k,v in bxs.items():
    for i,x in enumerate(v):
        print(k,i,x)
        a+=(k+1)*(i+1)*(x[1])
        
print(a)
