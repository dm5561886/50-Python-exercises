def sum_numbers(str_data):

    # str_isdigit = []
    # for i in str_data.split():
    # if i.isdigit():
    # str_isdigit.append(int(i))
    # return sum(str_isdigit)
    # [值或運算式 for 值 in 容器 if 條件判斷式]
    return sum([int(i) for i in str_data.split() if i.isdigit()])


print(sum_numbers('10 abc 20 de44 30 55fg 40'))
