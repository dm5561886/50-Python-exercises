def record_rainfall():
    rainfall_data = {}
    while True:
        city_name = input('輸入城市:')
        rainfall = input('輸入雨量(mm):')
        if city_name == '':
            break

        if rainfall == '':
            rainfall = 0

        if city_name in rainfall_data:
            rainfall_data[city_name] += int(rainfall)
        else:
            rainfall_data[city_name] = int(rainfall)

    for city, rain in rainfall_data.items():
        print(f'{city}: {rain}mm')


record_rainfall()
