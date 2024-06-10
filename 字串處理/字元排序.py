def strsort(word):
    # key=str.lower (取得所有字母的小寫格式來排序)
    return ''.join(sorted(word, key=str.lower))


print(strsort('python'))
