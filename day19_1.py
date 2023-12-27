from sys import stdin

wf={}

for li in stdin:
    li=li.strip()
    if not li:break
    nm,df=li.split('{')
    df=df[:-1]
    f=[]
    pts=df.split(',')
    for p in pts[:-1]:
        f.append(p.split(':'))
    f.append((None,pts[-1]))
    wf[nm]=f

ans=0
for li in stdin:
    pts=li.strip()[1:-1].split(',')
    ev={}
    for p in pts:
        nm,v=p.split('=')
        ev[nm]=int(v)
    f='in'
    while f not in ['A','R']:
        fl=wf[f]
        for ft,ds in fl[:-1]:
            print(ft,ds,ev)
            if eval(ft,None,ev):
                break
        else:
            ds=fl[-1][1]
        f=ds
    if f =='A':
        # print(li,ev.values())
        ans+=sum(ev.values())

print(ans)
