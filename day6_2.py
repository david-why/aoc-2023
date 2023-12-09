from math import *

t,d=open('day6.in').read().splitlines()
t=int(t.split(None,1)[1].replace(' ',''))
d=int(d.split(None,1)[1].replace(' ',''))

s=((-t+sqrt(t*t-4*d))/-2)
e=((-t-sqrt(t*t-4*d))/-2)
print(ceil(e)-ceil(s))
