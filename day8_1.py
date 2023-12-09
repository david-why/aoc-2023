s=open('day8.in').read().splitlines()

dirs= s[0]

nds={}

for li in s[1:]:
    tg,nn =li.split(' = ')
    gl,gr = nn.strip('()').split(', ')
    nds[tg]=(gl,gr)

i=0
c='AAA'
while c!='ZZZ':
    d='LR'.index(dirs[i%len(dirs)])
    i+=1
    c=nds[c][d]

print(i)
