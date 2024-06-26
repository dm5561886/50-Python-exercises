def alphabetize_names(people):
    # 先用性排序，再用名排序
    for person in sorted(people, key=lambda d: (d[1], d[0])):
        print(f'{person[1]},{person[0]}:{person[2]}')


people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
]

alphabetize_names(people)
