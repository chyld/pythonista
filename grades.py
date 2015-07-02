n = int(input())
people = {}

for person in range(n):
    person, g1, g2, g3 = input().split()
    people[person] = (float(g1) + float(g2) + float(g3)) / 3

print("{0:.2f}".format(people[input()]))
