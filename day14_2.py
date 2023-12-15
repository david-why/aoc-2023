s=open('day14.in').read().splitlines()
s=[list(x) for x in s]

ls={}
m={}

def roll(i,j,a,b):
    c=s[i][j]
    if c!='O':return
    while i+a>=0 and i+a<len(s) and j+b>=0 and j+b<len(s[0]) and s[i+a][j+b]=='.':
        s[i][j]='.'
        s[i+a][j+b]='O'
        i+=a
        j+=b

def calc():
    ans=0
    for i in range(len(s)):
        for j in range(len(s[0])):
            ans += (len(s)-i)*(s[i][j]=='O')
    return ans

x=0
while True:
    h=''.join(''.join(x) for x in s)
    if h in ls:
        break
    ls[h]=x
    m[x]=calc()
    print('\n'.join(''.join(s) for s in s),end='\n\n')
    for a,b in [(-1,0), (0,-1), (1,0), (0,1)]:
        for i in range(len(s)) if a<=0 else range(len(s)-1,-1,-1):
            for j in range(len(s[0])) if b<=0 else range(len(s[0])-1,-1,-1):
                roll(i,j,a,b)
    x+=1
    # if x>=1000000000:break

# 10
# 3
# 7

dif=x-ls[h]
idx=ls[h]+(1000000000-x)%dif
print(m)
print(ls[h])
print(m[idx])
