def flatten(two_list):
    # data_list = []
    # for i in two_list:
    # for j in i:
    # data_list.append(j)
    # return data_list
    return [j for i in two_list for j in i]


print(flatten([[1, 2], [3, 4]]))
