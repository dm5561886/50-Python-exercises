class Cat():
    # 建構子(Constructor)
    def __init__(self):  # (self, 物件初始化參數)
        # 屬性(Attribute)
        self.color = 'red'
        self.weight = 'heavy'

    # 方法(Method)
    def run(self):  # (self, 自訂義所需參數)
        print('cat  runing')


# 實體化物件
nash = Cat()  # nash是Cat的具體化物件(object)
nash.run()    # 使用物件裡的方法
