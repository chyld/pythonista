from collections import defaultdict

n, m = [int(x) for x in input().split()]
d = defaultdict(list)

for x in range(n):
    letter = input()
    d[letter].append(str(x+1))

for x in range(m):
    letter = input()
    a = d[letter]
    if len(a) > 0:
        print(' '.join(a))
    else:
        print(-1)

