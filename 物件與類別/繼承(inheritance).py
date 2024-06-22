class Grandfather():
    def __init__(self):
        self.head = 'Big'

    def work(self):
        print('No hard')

# Son繼承 Father類


class Father(Grandfather):
    def __init__(self):
        self.head = 'Big'

    # 方法覆寫(Method Overriding)
    def work(self):
        print('work hard')


class Son(Father):
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'

    def play(self):
        print('play hard')


nash = Son()
nash.work()
nash.play()
