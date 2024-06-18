def flipped_dict(dict_data):
    # {運算式, 運算式 for 鍵,值 in 容器}
    return {value: key for key, value in dict_data.items()}


print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))
