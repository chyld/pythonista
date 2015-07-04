import re
n = int(input())
for _ in range(n):
    is_good = 'YES' if re.match('^[789]{1}[0-9]{9}$', input()) else 'NO'
    print(is_good)
