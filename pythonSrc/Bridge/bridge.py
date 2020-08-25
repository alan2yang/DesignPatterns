from abc import ABCMeta, abstractmethod


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        raise NotImplemented()


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        raise NotImplemented()


class Rectangle(Shape):
    name = '矩形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = '圆'

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f'绘制红色的{shape.name}')


class Purple(Color):
    def paint(self, shape):
        print(f'绘制紫色的{shape.name}')


if __name__ == '__main__':
    rectangle = Rectangle(Red())
    rectangle.draw()

    circle = Circle(Purple())
    circle.draw()

