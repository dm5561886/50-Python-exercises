class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Scoop_Maker:
    def create(self, flavors):
        return [Scoop(flavor) for flavor in flavors]


scoop_maker = Scoop_Maker()  # 產生冰淇淋製造機的物件
scoops = scoop_maker.create(['巧克力', '香草', '薄荷'])

for scoop in scoops:
    print(scoop, scoop.flavor)
