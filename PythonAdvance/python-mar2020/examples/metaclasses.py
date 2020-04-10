class MyMeta(type):
    @classmethod
    def __new__(mcs, *args, **kwargs):
        return_value = super().__new__(*args, **kwargs)
        print(f'Inside MyMeta.__new__: {mcs}, {args}, {kwargs}, {return_value}')
        return return_value

    def __call__(cls, *args, **kwargs):
        print('Entering MyMeta.__call__ method')
        return_value = super().__call__(*args, **kwargs)
        print(f'Inside MyMeta.__call__: {cls}, {args}, {kwargs}, {return_value}')
        return return_value


class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print('Inside MyClass.__new__')
        return super().__new__(cls)

    def __init__(self, attr):
        print('Inside MyClass.__init__')
        self.attr = attr


obj = MyClass(10)
