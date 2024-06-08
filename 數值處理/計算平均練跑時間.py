def run_timing():
    run_count = 0
    toatal_time = 0.0
    while True:
        run_time = input('請輸入跑10km時間或按Enter離開:')
        if run_time == '':
            break
        try:
            run_time_value = float(run_time)
            toatal_time += run_time_value
            run_count += 1
        # 如果資料轉換錯誤，攔截該錯誤並列印錯誤訊息
        except Exception as e:
            print('產生錯誤:', e)

    if run_count > 0:
        average_time = toatal_time / run_count
    else:
        # 如未輸入數值，將結果設為0
        average_time = 0.0

    print(f'跑{run_count}次的平均時間為{average_time}分鐘')


run_timing()
