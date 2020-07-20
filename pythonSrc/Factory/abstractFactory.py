from abc import ABCMeta, abstractmethod


class User:
    """
    User Model
    """


class IUser(metaclass=ABCMeta):

    @abstractmethod
    def insert_user(self, user):
        """
        insert user
        """
        pass

    @abstractmethod
    def get_user(self):
        """
        get user
        """
        pass


class SqlserverUser(IUser):
    def insert_user(self, user):
        print("insert user into sqlserver")

    def get_user(self):
        print("get user from sqlserver")


class MysqlUser(IUser):
    def insert_user(self, user):
        print("insert user into mysql")

    def get_user(self):
        print("get user from mysql")


class Department:
    """
    Department Model
    """


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def insert_department(self, department):
        """
        insert department
        """

    @abstractmethod
    def get_department(self):
        """
        get department
        """


class SqlserverDepartment(IDepartment):
    def insert_department(self, department):
        print("Insert department into Sqlserver")

    def get_department(self):
        print("Get department from Sqlserver")


class MysqlDepartment(IDepartment):
    def insert_department(self, department):
        print("Insert department into Mysql")

    def get_department(self):
        print("Get department from Mysql")


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self):
        """
        create user
        """

    @abstractmethod
    def create_department(self):
        """
        create department
        """


class SqlserverFactory(IFactory):
    def create_user(self):
        return SqlserverUser()

    def create_department(self):
        return SqlserverDepartment()


class MysqlFactory(IFactory):
    def create_user(self):
        return MysqlUser()

    def create_department(self):
        return MysqlDepartment()


if __name__ == '__main__':
    ifactory = SqlserverFactory()
    iuser = ifactory.create_user()
    iuser.insert_user(User())
    iuser.get_user()
