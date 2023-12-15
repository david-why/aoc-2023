s=open('day15.in').read().replace('\n', '').split(',')

def h(s):
    a=0
    for c in s:
        a=(a+ord(c))*17%256
    return a

print(sum(map(h, s)))
