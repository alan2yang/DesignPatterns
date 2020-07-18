from abc import ABCMeta, abstractmethod


class AbstractProductA(object):
    """
    抽象产品, 可能拥有多种实现
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "ProductA: %s" % self.name


class ConcreteProductA1(AbstractProductA):
    pass


class ConcreteProductA2(AbstractProductA):
    pass


class AbstractProductB(object):
    """
    抽象产品, 可能拥有多种实现
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "ProductB: %s" % self.name


class ConcreteProductB1(AbstractProductB):
    pass


class ConcreteProductB2(AbstractProductB):
    pass


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_productA(self):
        pass

    @abstractmethod
    def create_productB(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_productA(self):
        return ConcreteProductA1("PA1")

    def create_productB(self):
        return ConcreteProductB1("PB1")


class ConcreteFactory2(AbstractFactory):
    def create_productA(self):
        return ConcreteProductA2("PA2")

    def create_productB(self):
        return ConcreteProductB2("PB2")


if __name__ == '__main__':
    factory = ConcreteFactory1()
    productA = factory.create_productA()
    print(productA)
    productB = factory.create_productB()
    print(productB)
