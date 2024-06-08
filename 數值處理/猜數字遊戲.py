import random


def guessing_game():
    answer = random.randint(0, 99)

    while True:
        str_num = input("猜數字(0~99)或輸入'離開'退出遊戲:")
        if str_num == '離開':
            break
        # 使用isdigit()檢查輸入字串是否能轉整數
        elif str_num.isdigit():
            num = int(str_num)
            if num > answer:
                print('猜得太高，再試一次')
            elif num < answer:
                print('猜得太低，再試一次')
            else:
                print(f'猜對了答案是 {answer}')
                break
        else:
            print("無效輸入，請輸入0到99之間的數字或'離開'")


guessing_game()
