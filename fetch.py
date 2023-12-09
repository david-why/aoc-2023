import argparse
import requests

import os

ap = argparse.ArgumentParser()

ap.add_argument('year', type=int)
ap.add_argument('day', type=int)

args = ap.parse_args()
year = args.year
day = args.day

cookie = open('cookie.txt').read().strip()

s = requests.Session()
r = s.get(
    f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': cookie}
)

with open(f'day{day}.in', 'w') as f:
    f.write(r.text)

if not os.path.exists(f'day{day}_1.py'):
    with open(f'day{day}_1.py', 'a') as f:
        f.write(f"s=open('day{day}.in').read().splitlines()\n")
if not os.path.exists(f'day{day}_2.py'):
    with open(f'day{day}_2.py', 'a') as f:
        f.write(f"s=open('day{day}.in').read().splitlines()\n")
