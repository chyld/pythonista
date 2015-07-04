import re
n = int(input())
emails = []
for _ in range(n):
    emails.append(input())

emails = list(filter(lambda e: re.match('^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', e), emails))
emails.sort()
print(emails)
