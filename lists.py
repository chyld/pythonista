l = []
for cmd in range(int(input())):
    args = input().split()
    if args[0] == 'insert':
        l.insert(int(args[1]), int(args[2]))
    elif args[0] == 'remove':
        l.remove(int(args[1]))
    elif args[0] == 'append':
        l.append(int(args[1]))
    elif args[0] == 'sort':
        l.sort()
    elif args[0] == 'pop':
        l.pop()
    elif args[0] == 'reverse':
        l.reverse()
    elif args[0] == 'print':
        print(l)
