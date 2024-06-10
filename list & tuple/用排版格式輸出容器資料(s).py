def sorted_grades(grades):
    # 按照成績大到小(reverse=True)排序
    grades.sort(key=lambda a: a[2], reverse=True)
    output = []
    for first, last, grade in grades:
        # 字串(s)12格、字串(s)10格、浮點數(f)小數四捨五入到第1位
        output.append(f'{last:12s}{first:10s}{grade:.1f}')

    return '\n'.join(output)


grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
]
print(sorted_grades(grades))
