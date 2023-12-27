s=open('day20.in').read().splitlines()

mod={}
br=[]
for li in s:
    print(li)
    fr,to=li.split(' -> ')
    to=to.split(', ')
    mod[fr[1 if fr[0] in '&%' else 0:]]=(fr[0],to)

inp={}
for m in mod:
    inp[m]=[]
    for x in mod:
        if m in mod[x][1]:
            inp[m].append(x)

#0 lo/off, 1 hi/on
mem={}
for m in mod:
    if mod[m][0]=='&':
        mem[m]={}
        for i in inp[m]:
            mem[m][i]=0
    elif mod[m][0]=='%':
        mem[m]=0

ans=[0,0]
for _ in range(1000):
    ans[0]+=1
    q:list=[('broadcaster',0,'_button')]
    while q:
        m,sig,fr=q.pop(0)
        if m not in mod:continue
        if mod[m][0]=='%':
            if not sig:
                mem[m]=1-mem[m]
                for x in mod[m][1]:
                    q.append((x,mem[m],m))
                    ans[mem[m]]+=1
        elif mod[m][0]=='&':
            mem[m][fr]=sig
            sd=1-int(all(mem[m].values()))
            for x in mod[m][1]:
                q.append((x,sd,m))
                ans[sd]+=1
        elif mod[m][0]=='b':
            for x in mod[m][1]:
                q.append((x,sig,m))
                ans[sig]+=1
    # if _<8:
    #     print(ans)

print(ans)
print(ans[0]*ans[1])
