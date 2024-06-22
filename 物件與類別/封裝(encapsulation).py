class Son():
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
        self.__IQ = '300'  # 封裝屬性

    def play(self):
        print('play hard')

    def hungry(self):
        self.__eat()

    def __eat(self):  # 封裝方法
        print('good')


nash = Son()
nash.play()  # play hard
nash.hungry()  # good
nash._eat()  # 實體物件無法呼叫私有屬性和方法
nash.__IQ()  # 實體物件無法呼叫私有屬性和方法
