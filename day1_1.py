t=open('day1.in').read().splitlines()

m = 0
for s in t:
    x = list(filter(str.isdigit, s))
    if x:
        m += int(x[0]) * 10 + int(x[-1])

print(m)
