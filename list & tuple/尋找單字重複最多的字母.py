def most_repeated_letter(string):
    string_count = {}
    for str in string:
        if str in string_count:
            string_count[str] += 1
        else:
            string_count[str] = 1

    # 出現次數最多的字母及次數
    max_string_count = max(string_count, key=string_count.get)
    max_count = string_count[max_string_count]
    print(f'{max_string_count}重複了{max_count}次')


most_repeated_letter('independence')
