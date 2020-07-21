from abc import ABCMeta,abstractmethod


class Pen:
    """

    """


class Graphics:
    """

    """


class PersonBuilder(metaclass=ABCMeta):
    def __init__(self,p,g):
        self.pen = p
        self.graphics= g

    @abstractmethod
    def build_head(self):
        """
        build head
        """

    @abstractmethod
    def build_body(self):
        """
        build body
        """


class PersonThinBuilder(PersonBuilder):
    def build_head(self):
        print("build thin head")

    def build_body(self):
        print("build thin body")


class PersonDirector:
    """
    该类只起到组织的作用，创建方法是调用传入对象自己的
    """
    def __init__(self,pb):
        self.person_builder = pb

    def create_person(self):
        self.person_builder.build_head()
        self.person_builder.build_body()


if __name__ == '__main__':
    person_builder = PersonThinBuilder(Pen(),Graphics())
    director = PersonDirector(person_builder)
    director.create_person()

