Dwayne = [
    ['algebra', 40],
    ['geometry', 60],
    ['math', 80],
    ['history', 100],
    ['physics', 90],
    ["chemistry", 50],
    ['literature', 70]
]

Rock = [
    ['algebra', 20],
    ['geometry', 20],
    ['math', 60],
    ['history', 40],
    ['physics', 15],
    ["chemistry", 10],
    ['literature', 30]
]

Johnson = [
    ['algebra', 90],
    ['geometry', 40],
    ['math', 85],
    ['history', 65],
    ['physics', 30],
    ["chemistry", 30],
    ['literature', 70]
]

Dwayne = dict(Dwayne)
Rock = dict(Rock)
Johnson = dict(Johnson)
students = {
    'Dwayne': Dwayne,
    'Rock': Rock,
    'Johnson': Johnson
}

avg_mark_students = {
    'Dwayne': int(sum(Dwayne.values()) / len(Dwayne)),
    'Rock': int(sum(Rock.values()) / len(Rock)),
    'Johnson': int(sum(Johnson.values()) / len(Johnson)),
}
for key, value in students.items():
    print(f'{key} : {value}\n Средний балл:  {sum(value.values()) / len(value.values())}')

for key, value in avg_mark_students.items():
    if value == max(avg_mark_students.values()):
        best_student = key
print(f'Лучшим студентом является : {best_student}')

