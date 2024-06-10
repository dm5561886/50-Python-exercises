def rot13(word):
    output = []
    for i in word.lower():
        new_word = ord(i)+13
        # 若移動超過字母'Z'的ASCII值，往回減26(從A算)
        if new_word > ord('z'):
            new_word -= 26
        output.append(chr(new_word))
    return ''.join(output)


print(rot13('apple'))
