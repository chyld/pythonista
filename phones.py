n = int(input())
phones = []
for _ in range(n):
    phone = input()
    phones.append(phone[len(phone)-10:])

phones.sort()

for phone in phones:
    print("+91 {0} {1}".format(phone[:5], phone[5:]))
