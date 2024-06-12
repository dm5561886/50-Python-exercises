def read_final_line(filename):
    # 開啟文字檔
    f = open(filename, 'r')
    for line in f:
        pass
    f.close()
    # 回傳最後一行文字
    return line


print(read_final_line(r'C:\路徑\login.log'))
