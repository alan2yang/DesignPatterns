
from abc import abstractmethod,ABCMeta


class Adaptee:
    """
    需要被适配的类
    """
    def special_request(self):
        print("I am special")


class Target(metaclass=ABCMeta):
    """
    统一接口
    """
    @abstractmethod
    def request(self):
        pass


class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.special_request()


if __name__ == '__main__':
    a = Adapter()
    a.request()
