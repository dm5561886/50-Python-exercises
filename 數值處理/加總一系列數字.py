def my_sum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4, 5))
