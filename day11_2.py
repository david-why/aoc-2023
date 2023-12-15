s = open('day11.in').read().splitlines()

colemp = [all(s[i][j] == '.' for i in range(len(s))) for j in range(len(s[0]))]
rowemp = [all(s[i][j] == '.' for j in range(len(s[0]))) for i in range(len(s))]

p = []
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == '#':
            p.append((i, j))

ans = 0
for a, b in p:
    for c, d in p:
        if a == c and b == d:
            continue
        ans += (
            abs(a - c)
            + abs(b - d)
            + (1000000-1)
            * (sum(colemp[min(b, d) : max(b, d)]) + sum(rowemp[min(a, c) : max(a, c)]))
        )

print(ans // 2)
