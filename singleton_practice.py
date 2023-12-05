def singleton_test(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton_test
class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello")


class Teacher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __int__(self, name):
        self.name = name


if __name__ == '__main__':
    # s1 = Student("c")
    # s2 = Student("suo")
    #
    # print(s1 is s2)
    t1 = Teacher("chaozhou")
    t2 = Teacher("praveen")
    print(t1 is t2)
