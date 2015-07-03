cases = int(input())

for case in range(cases):
    input()
    col = []
    row = [int(x) for x in input().split()]
    while True:
       if len(row) >= 2:
        m = max(row[0], row[-1])
        if row[0]== m:
            i = 0
        else:
            i = -1

        if len(col) == 0 or col[-1] >= m:
            col.append(m)
            del row[i]
        else:
            print('No')
            break
       elif len(row) == 1:
        if len(col) == 0 or col[-1] >= row[0]:
            col.append(row.pop())
        else:
            print('No')
            break
       else:
        print('Yes')
        break
