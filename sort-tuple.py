people = []
n = int(input())
for i in range(n):
    first, last, age, gender = input().split()
    salutation = 'Mr.' if gender == 'M' else 'Ms.'
    full = salutation + ' ' + first + ' ' + last
    age = age.zfill(4) + chr(i + 97)
    people.append((age, full))

people.sort(key=lambda tup: tup[0])

for person in people:
    print(person[1])
