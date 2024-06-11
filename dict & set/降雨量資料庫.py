def record_rainfall():
    rainfall_data = {}
    while True:
        city_name = input('輸入城市:')
        rainfall = input('輸入雨量(mm):')
        if city_name == '':
            break

        if rainfall == '':
            rainfall = 0

        # 使用get抓取某城市降雨量，如果無此件就回傳0
        rainfall_data[city_name] = rainfall_data.get(
            city_name, 0)+int(rainfall)

    for city, rain in rainfall_data.items():
        print(f'{city}: {rain}mm')


record_rainfall()
