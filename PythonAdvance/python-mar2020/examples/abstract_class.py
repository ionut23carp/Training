import abc


class MyABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abstract_method(self):
        pass


class ConcreteClass(MyABC):
    def abstract_method(self):
        return 'concrete value'


obj = ConcreteClass()
