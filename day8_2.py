s=open('day8.in').read().splitlines()

dirs= s[0]

nds={}

for li in s[1:]:
    tg,nn =li.split(' = ')
    gl,gr = nn.strip('()').split(', ')
    nds[tg]=(gl,gr)

i=0
c=list(filter(lambda x:x.endswith('A'), nds))
pts = []
for x in c:
    print(x)
    v=set()
    p=[]
    i=0
    while (x,i%len(dirs)) not in v:
        v.add((x,i%len(dirs)))
        if x.endswith('Z'):
            p.append((x,i))
        x=nds[x]['LR'.index(dirs[i%len(dirs)])]
        i+=1
    pts.append(p)
from math import lcm
print(lcm(*(x[0][1] for x in pts)))
# while True:
#     d='LR'.index(dirs[i%len(dirs)])
#     i+=1
#     nc=[]
#     for x in c:
#         nc.append(nds[x][d])
#     c=nc
#     ok=True
#     for x in c:
#         if not x.endswith('Z'):
#             ok=False;break
#     if ok:break

# print(i)
