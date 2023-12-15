s=open('day14.in').read().splitlines()
s=[list(x) for x in s]

def roll(i,j):
    c=s[i][j]
    if c!='O':return
    while i>0 and s[i-1][j]=='.':
        s[i][j]='.'
        s[i-1][j]='O'
        i-=1

for i in range(len(s)):
    for j in range(len(s[0])):
        roll(i,j)

ans=0
for i in range(len(s)):
    for j in range(len(s[0])):
        ans += (len(s)-i)*(s[i][j]=='O')
        
print(ans)
