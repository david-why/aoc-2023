s=open('day9.in').read().splitlines()

d=[list(map(int,x.split())) for x in s]

def fv(x):
    if not any(x):
        return 0
    return x[0] - fv([x[i]-x[i-1] for i in range(1,len(x))])

ans = sum(map(fv,d))

print(ans)
