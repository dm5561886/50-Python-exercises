def mysum(*items):
    # 判斷字串是否為空
    if len(items) == 0:
        return items
    # 先取得索引 0元素，讓變數獲得同樣的型別
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(mysum(10, 20, 30, 40))
