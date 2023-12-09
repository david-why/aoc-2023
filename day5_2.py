import bisect

s=open('day5.in').read().splitlines()

ans=0

seeds = list(map(int,s[0].split()[1:]))
seeds=[(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]
seeds.sort()
nsee =[]

ln=2
while ln<len(s):
    #print(seeds)
    #print(s[ln])
    ln+=1
    tr ={}
    lst=[]
    sp= []
    while ln<len(s) and s[ln]:
        line=s[ln]
        ln+=1
        ds,ss,le=map(int,line.split())
        lst.append((ss,ds,le))
        sp.append(ss)
        sp.append(ss+le)
    ln+=1
    lst.sort()
    sp = list(set(sp))
    sp.sort()
    sc = list(seeds)
    seeds =[]
    #print('sp:',sp)
    for a,b in sc:
        spi =bisect.bisect_right(sp,a)
        pa=a
        while spi<len(sp) and sp[spi]<b:
            seeds.append((pa,sp[spi]))
            pa=sp[spi]
            spi+=1
        if pa!=b:
            seeds.append((pa,b))
    #print('sect:', seeds)
    seeds.sort()
    for ss,ds,le in lst:
        for sl,sr in list(seeds):
            if sl<ss:  # before me
                seeds.remove((sl,sr))
                nsee.append((sl,sr))
                continue
            if sl>=ss+le:
                break
            seeds.remove((sl,sr))
            nsee.append((sl-ss+ds,sr-ss+ds))
    nsee.extend(seeds)
    nsee.sort()
    seeds = nsee
    nsee=[]

#print(seeds)
print(min(seeds))
