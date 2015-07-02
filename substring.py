str = input()
sub = input()
count = 0
for i in range(len(str)):
    count += str.count(sub, i, i + len(sub))

print(count)
