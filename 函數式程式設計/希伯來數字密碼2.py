import string


def gematria_dict():
    return {char: index
            for index, char
            in enumerate(string.ascii_lowercase, 1)}


GEMATRIA = gematria_dict()


def gematria_value(word):  # 計算希伯來數值的函式
    return sum(GEMATRIA[char]
               for char in word.lower()
               if char in GEMATRIA)


def gematria_equal_words(input_word, filename):
    input_value = gematria_value(input_word)
    with open(filename, 'r', encoding='utf-8') as f:
        return [word
                for line in f
                for word in line.lower().split()
                if input_value == gematria_value(word)]


print(gematria_equal_words('programming', r'C:\路徑\book.txt'))
