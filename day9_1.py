s=open('day9.in').read().splitlines()

d=[list(map(int,x.split())) for x in s]

def fv(x):
    if not any(x):
        return 0
    return x[-1] + fv([x[i+1]-x[i] for i in range(len(x)-1)])

ans = sum(map(fv,d))

print(ans)
