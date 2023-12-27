s=open('day24.in').read().splitlines()

h=[]

for li in s:
    p,v=li.split('@')
    h.append([[int(x) for x in p.split(',')], [int(x) for x in v.split(',')]])

MIN=200000000000000
MAX=400000000000000

def sv(i,j):
    if i==j:return 0
    (x01,y01,_),(vx1,vy1,_)=h[i]
    (x02,y02,_),(vx2,vy2,_)=h[j]
    if vx1/vy1==vx2/vy2:
        return 0
    x=(y02-x02*vy2/vx2-y01+x01*vy1/vx1)/(vy1/vx1-vy2/vx2)
    y=y02-x02*vy2/vx2+vy2/vx2*x
    if (x-x01)/vx1<0 or (x-x02)/vx2<0:return 0
    if MIN<=x<=MAX and MIN<=y<=MAX:
        # print(i,j)
        return 1
    return 0

ans=0
for i in range(len(h)):
    for j in range(len(h)):
        if i!=j:
            ans+=sv(i,j)

print(ans//2)
