t=open('day1.in').read().splitlines()

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def calc(s:str):
    m=0
    idx=1e9
    d=0
    for i in range(10):
        f=s.find(numbers[i])
        g=s.find(str(i))
        if idx>g and g!=-1:
            d=i
            idx=g
        if idx>f and f!=-1:
            d=i
            idx=f
    if idx==1e9:
        return 0
    m+=10*d
    idx=-1
    d=0
    for i in range(10):
        f=s.rfind(numbers[i])
        g=s.rfind(str(i))
        if idx<g:
            d=i
            idx=g
        if idx<f:
            d=i
            idx=f
    return m+d

print(sum(map(calc, t)))
