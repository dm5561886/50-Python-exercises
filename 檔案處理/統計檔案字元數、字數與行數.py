def wordcount(filename):
    result = {
        'Characters': 0,
        'Words': 0,
        'Unique words': 0,
        'Lines': 0,
    }
    unique_words = set()

    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            # 行數
            result['Lines'] += 1
            # 字元數
            result['Characters'] += len(line)
            # 累加單字數
            result['Words'] += len(words)
            # 過濾不重複單字
            unique_words.update(words)

        result['Unique words'] = len(unique_words)

    for key, value in result.items():
        print(f'{key}: {value}')


wordcount(r'.\data\text.txt')
