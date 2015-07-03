from collections import OrderedDict
d = OrderedDict()

length = int(input())

for n in range(length):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))
print(' '.join([str(v) for k,v in d.items()]))
