import copy


class SelfReferenceEntity(object):
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_object, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_object = some_list_of_object
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        浅拷贝对象
        """
        some_list_of_objects = copy.copy(self.some_list_of_object)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)

        return new

    def __deepcopy__(self, memodict={}):
        """
        深拷贝对象
        """
        some_list_of_objects = copy.deepcopy(self.some_list_of_object, memodict)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memodict)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        return new


if __name__ == '__main__':
    # for item in SelfReferenceEntity.__dict__:
    #     proper = getattr(SelfReferenceEntity,item,None)
    #     if callable(proper):
    #         print(f"{item} is func")
    #     else:
    #         print(f"{item} is not callable")
    someObject = SelfReferenceEntity()
    SC = SomeComponent(12, ["new", "test", "aa"], someObject)
    someObject.set_parent(SC)
