from datetime import date


# class Person(models.Model):
#     first_name = models.CharField(max_length=255, null=True)
#     last_name = models.CharField(max_length=255, null=False)
#     date_of_birth = models.DateField(default=now)


class ChoiceField:
    def __init__(self, choices):
        self.choices = choices
        self.values = {}

    def __set__(self, instance, value):
        if value not in self.choices:
            raise Exception('Not a valid choice')
        # setattr(instance, self.name, value)
        self.values[instance] = value

    def __get__(self, instance, owner):
        # return getattr(instance, self.name)
        return self.values[instance]

    # def __set_name__(self, owner, name):
    #     self.name = f'_{name}'


class Person:
    __slots__ = ['first_name', '__date_of_birth']

    COUNTER = 0
    MIN_DOB = date(1900, 1, 1)
    hair_color = ChoiceField(choices=('blonde', 'brunette', 'red'))

    def __init__(self, name, date_of_birth_param, hair_color):
        self.first_name = name
        self.date_of_birth = date_of_birth_param
        self.hair_color = hair_color

        self.increment_count()

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        if value < self.MIN_DOB:
            raise Exception('Invalid date of birth')
        self.__date_of_birth = value

    # date_of_birth = property(get_date_of_birth, set_date_of_birth)

    @property
    def age(self):
        return int((date.today() - self.date_of_birth).days / 365.25)

    def greet(self):
        print(f'Hello! I am {self.first_name}')

    @classmethod
    def increment_count(cls):
        cls.COUNTER += 1

    @classmethod
    def print_message(cls):
        print(f'Class {cls.__name__} has created {cls.COUNTER} objects.')

    @staticmethod
    def say_hello():
        print('Hello!')

    @staticmethod
    def __hello():
        print('Hi!')

    def __str__(self):
        return f'Person instance'

    def __repr__(self):
        return f'Person instance {id(self)}'

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth


class Student(Person):
    COUNTER = 0
    university = ChoiceField(choices=['Politehnica București',
                                      'ASE București',
                                      'Universitatea București'])

    def __init__(self, name, date_of_birth, hair_color, university):
        super().__init__(name, date_of_birth, hair_color)
        self.university = university

    @staticmethod
    def say_hello():
        print('Hello! This class is for students')

    @classmethod
    def increment_count(cls):
        super().increment_count()
        super().increment_count()


if __name__ == '__main__':
    person1 = Person("Ana", date(1989, 2, 5), 'blonde')
    person2 = Person('Jane', date(1999, 3, 5), 'red')

    # print(person1)
    # print('Instance attribute:', person1.first_name)
    # print('Class attribute:', person1.COUNTER, Person.COUNTER)
    # person1.greet()
    # # Person.say_hello(person1)
    # Person.print_message()
    # person1.print_message()
    # Person.say_hello()
    # person1.say_hello()

    # print(str(person1))
    # print(repr(person1))
    # print(person1)

    print(person1.hair_color, person2.hair_color)

    print(person1 < person2)
    print(person1 > person2)

    # Person.__hello()

    # person2.date_of_birth = date(1997, 1, 1)
    # print(person2.date_of_birth)
    #
    # print(person1.age)
    # print(person2.age)
    #
    student1 = Student("Maria", date(2001, 2, 6), 'red', 'Politehnica București')

    print(student1.hair_color, student1.university)

    # Cannot do that because we defined __slots__ inside Person class
    # person1.new_attr = 100
    # print(person1.new_attr)

    # print(student1.university, student1.first_name)
    # print(student1.age)
    # Student.print_message()
    # Student.say_hello()
    # Student.increment_count()
