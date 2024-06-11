def unique_num_len(number):
    # 先轉set找出不重複元素，再用 len()計算個數
    return len(set(number))


number = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(unique_num_len(number))
