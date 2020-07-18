class Operation(object):
    @property
    def number_a(self):
        return self.__number_a

    @number_a.setter
    def number_a(self, value):
        self.__number_a = value

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, value):
        self.__number_b = value

    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        return self.number_a + self.number_b


class OperationSub(Operation):
    def get_result(self):
        return self.number_a - self.number_b


# 如果要添加其他的计算方法，可以再添加其他类
# 方便扩展


class OperationFactory(object):
    @staticmethod
    def create_operation(operationStr):
        if operationStr == "+":
            return OperationAdd()
        elif operationStr == "-":
            return OperationSub()


if __name__ == '__main__':
    op = OperationFactory.create_operation("+")
    op.number_b = 10
    op.number_a = 100
    print(op.get_result())
