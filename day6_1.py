t,d=open('day6.in').read().splitlines()
t=[int(x) for x in t.split()[1:]]
d=[int(x) for x in d.split()[1:]]

ans=1
for t,d in zip(t,d):
    cnt=0
    for i in range(t):
        v=(t-i)*i
        if v>d:
            cnt+=1
    ans*=cnt
print(ans)
