def menu(**options):
    # 定義閉包函式(menu 物件)
    def menu_selector():
        option_str = '/'.join(options)
        while True:
            choice = input(f'選擇題目({option_str}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在')
    return menu_selector
