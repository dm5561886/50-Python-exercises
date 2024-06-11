menu = {
    '三明治': 50,
    '咖啡': 40,
    '沙拉': 30
}


def order_meal():
    toatal = 0
    while True:
        meals = input('請點餐:')
        if meals == '':
            print('結束點餐')
            break
        elif meals in menu:
            price = menu[meals]
            toatal += price
            print(f'{meals} {price}元, 總金額{toatal}')
        else:
            print(f'抱歉，無供應{meals}，請重新輸入')
    print(f'總金額為{toatal}')


order_meal()
