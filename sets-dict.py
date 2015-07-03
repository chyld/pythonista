from collections import defaultdict
d = defaultdict(int)
h = 0

input()

for n in input().split():
    d[n] += 1

for a in input().split():
    if a in d:
        h += d[a]

for b in input().split():
    if b in d:
        h -= d[b]

print(h)
