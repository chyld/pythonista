n = int(input())
students = {}

for i in range(n):
    name = input()
    grade = float(input())
    students[name] = grade

grades = list(students.values())
grades.sort()
lowest = grades[0]
lowest_count = grades.count(lowest)
second_lowest = grades[lowest_count]

results = []

for name, grade in students.items():
    if second_lowest == grade:
        results.append(name)

results.sort()

for name in results:
    print(name)
