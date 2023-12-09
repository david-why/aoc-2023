lines = open('day3.in').read().splitlines()

def adj(i,l, r):
    for j in range(max(l-1, 0), min(r+1, len(lines[0]))):
        if i>0 and lines[i-1][j]!='.':
            return True
        if i!=len(lines)-1 and lines[i+1][j] !='.':
            return True
    return l>0 and lines[i][l-1] !='.' or r<len(lines[0]) and lines[i][r] !='.'

ans = 0

for i in range(len(lines)):
    j = 0
    line = lines[i]
    while j<len(line):
        while j<len(line) and not line[j].isdigit():
            j+=1
        if j>=len(line):
            break
        num = 0
        start = j
        while j<len(line) and line[j].isdigit():
            num += int(line[j])
            num *= 10
            j += 1
        num //= 10
        if adj(i, start, j):
            ans += num

print(ans)
