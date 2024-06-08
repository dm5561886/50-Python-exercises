def hex_to_dec():
    input_carry = input('請輸入16進位數:')
    decimal = 0
    # 走訪字串取得索引和字串
    for index, num in enumerate(reversed(input_carry)):
        # 數字如果是0-9轉整數
        if num.isdigit():
            d_num = int(num)
        # A-F用ASCII碼計算成10-15
        else:
            d_num = ord(num.upper())-ord('A')+10

        # 個位數換10進位值並加總
        decimal += d_num*(16**index)
    print(f'十進位結果:{decimal}')


hex_to_dec()
