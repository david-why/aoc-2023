lines = open('day2.in').read().splitlines()

TOTAL = {'blue': 14, 'red': 12, 'green': 13}

ans = 0

for line in lines:
    _, idx_s, data = line.split(' ', 2)
    idx = int(idx_s[:-1])
    parts = data.split('; ')
    ok=True
    for part in parts:
        sets = part.split(', ')
        for st in sets:
            cnt, typ = st.split()
            cnt=int(cnt)
            if TOTAL[typ]<cnt:
                ok=False
    if ok:
        ans+=idx

print(ans)
