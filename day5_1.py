s=open('day5.in').read().splitlines()

ans=0

seeds = list(map(int,s[0].split()[1:]))
seeds.sort()
nsee =[]

ln=2
while ln<len(s):
    ln+=1
    tr ={}
    lst=[]
    while ln<len(s) and s[ln]:
        line=s[ln]
        ln+=1
        ds,ss,le=map(int,line.split())
        lst.append((ss,ds,le))
    ln+=1
    lst.sort()
    for ss,ds,le in lst:
        for sd in list(seeds):
            if sd<ss:
                seeds.remove(sd)
                nsee.append(sd)
            elif sd>=ss and sd<ss+le:
                seeds.remove(sd)
                nsee.append(sd-ss+ds)
            else:
                break
    nsee.extend(seeds)
    nsee.sort()
    seeds = nsee
    nsee=[]

print(min(seeds))
