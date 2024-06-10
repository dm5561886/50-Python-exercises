def most_repeated_letter(string):
    string_count = {}
    for str in string:
        if str in string_count:
            string_count[str] += 1
        else:
            string_count[str] = 1

    max_string_count = max(string_count, key=string_count.get)
    print(max_string_count)
    max_count = string_count[max_string_count]
    print(max_count)
    print(f'{max_string_count}重複了{max_count}次')


most_repeated_letter('independence')
