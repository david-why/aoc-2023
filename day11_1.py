s=open('day11.in').read().splitlines()

colemp = [all(s[i][j]=='.' for i in range(len(s))) for j in range(len(s[0]))]
rowemp = [all(s[i][j]=='.' for j in range(len(s[0]))) for i in range(len(s))]

mat = []
for i in range(len(s)):
    r=[]
    for j in range(len(s[0])):
        r.append(s[i][j])
        if colemp[j]:
            r.append(s[i][j])
    mat.append(r)
    if rowemp[i]:
        mat.append(['.' for _ in range(len(s[0])+colemp.count(True))])

a=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]=='#':
            a.append((i,j))

ans =0
for x,y in a:
    for c,d in a:
        if x==c and y==d:continue
        ans+=abs(x-c) +abs(y-d)

print(ans//2)
