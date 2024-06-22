class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)

    def show_content(self):
        return '/'.join(scoop.flavor for scoop in self.scoops)


bowl = Bowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))
bowl.add_scoop(Scoop('焦糖'), Scoop('抹茶'))
print(bowl.show_content())
