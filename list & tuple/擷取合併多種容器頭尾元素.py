def first_last(seq):
    # seq[:1]開頭元素切片 seq[-1:]最末元素的切片
    return seq[:1]+seq[-1:]


print(first_last([1, 2, 3, 4, 5]))
print(first_last('abcde'))
