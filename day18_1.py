s=open('day18.in').read().splitlines()

DIRS={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

i,j = (0,0)
w={(i,j)}

for l in s:
    d,c,_=l.split()
    for x in range(int(c)):
        i+=DIRS[d][0]
        j+=DIRS[d][1]
        w.add((i,j))
        
mni=min(w,key=lambda x:x[0])[0]-1
mnj=min(w,key=lambda x:x[1])[1]-1
mxi=max(w,key=lambda x:x[0])[0]+1
mxj=max(w,key=lambda x:x[1])[1]+1

i,j=mni,mnj
v=set()
q=[(i,j)]
while q:
    i,j=q.pop()
    if (i,j) in w:continue
    if (i,j) in v:continue
    if i<mni or i>mxi or j<mnj or j>mxj:continue
    v.add((i,j))
    for d in DIRS:
        q.append((i+DIRS[d][0],j+DIRS[d][1]))

print((mxi-mni+1)*(mxj-mnj+1)-len(v))
