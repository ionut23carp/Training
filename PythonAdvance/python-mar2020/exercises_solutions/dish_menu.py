

class Dish:
    def __init__(self, ind, name, price):
        self.ind = ind
        self.name = name
        self.price = price


class Menu(list):
    def add_dish(self, *args, **kwargs):
        super().append(*args, **kwargs)


d = Dish(0, 'Lasagna', 20)
m = Menu()
m.add_dish(d)
print(m[0])
print(d in m)

