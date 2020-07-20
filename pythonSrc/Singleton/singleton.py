import threading


class Singleton(object):
    instance = None
    lock = threading.RLock()  # 保证线程安全

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls.lock.acquire()
            if not hasattr(cls, "_instance"):  # 保证多线程情况下，多个线程同时进入到上层判断中
                cls._instance = super().__new__(cls)
            cls.lock.release()
        return cls._instance


if __name__ == '__main__':
    instance1 = Singleton()
    instance2 = Singleton()
    print(id(instance1))
    print(id(instance2))
