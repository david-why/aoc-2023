lines = open('day2.in').read().splitlines()

ans = 0

for line in lines:
    _, idx_s, data = line.split(' ', 2)
    idx = int(idx_s[:-1])
    parts = data.split('; ')
    nums= {'red': 0,'blue':0,'green':0}
    for part in parts:
        sets = part.split(', ')
        for st in sets:
            cnt, typ = st.split()
            cnt=int(cnt)
            nums[typ] = max(nums[typ], cnt)
    ans += nums['red']*nums['blue']*nums['green']

print(ans)
