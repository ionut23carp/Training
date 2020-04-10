from abc import ABC, abstractmethod


class PublicPlace(ABC):

    @abstractmethod
    def get_address(self):
        pass


class Restaurant(PublicPlace):
    count = 0

    def __init__(self, category, rating, address):
        self.category = category
        self.rating = rating
        self.address = address
        self.increase_count()

    @classmethod
    def increase_count(cls):
        cls.count += 1

    def get_address(self):
        print(self.address)

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value not in range(1, 6):
            raise Exception('Invalid rating')
        self.__rating = value

    def __str__(self):
        return f'Restaurant: {self.category} {self.rating}*'


class Dish:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Menu:
    def __init__(self, *dishes):
        self.dishes = list(dishes)

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __contains__(self, item):
        return item in self.dishes

    def __getitem__(self, item):
        return self.dishes[item]


if __name__ == '__main__':
    r1 = Restaurant('pizza', 3, 'Str. Bla 5')
    r2 = Restaurant('italian', 5, 'Str. Foo 5')
    assert Restaurant.count == 2
    print(r1)
    print(r2)

    r1.rating = 1
    print(r1)

    d1 = Dish(0, 'Lasagna', 20)
    d2 = Dish(1, 'Pizza 4F', 22)
    d3 = Dish(2, 'Mici x6', 12)

    m = Menu(d1, d2)
    m.add_dish(d3)

    assert d2 in m
    assert m[0] == d1
