def passwd_to_dict(filename):
    users = {}
    with open(filename) as f:
        for line in f:
            user_info = line.split(':')
            # 將帳號名稱(索引值0)和ID(索引值2)放入字典
            users.update({user_info[0]: user_info[2]})
    return users


print(passwd_to_dict(r'.\data\passwd.cfg'))
