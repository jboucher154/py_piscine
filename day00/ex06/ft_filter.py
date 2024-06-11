

class ft_filter:
    __doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    def __init__(self, func, iter):
        if not hasattr(iter, '__iter__'):
            raise TypeError(f"'{type(iter).__name__}' is not iterable")
        self.__func = func
        self.__data = iter
        self.__result = []

    def __filter(self):
        if self.__func is None:
            self.__result = [item for item in self.__data if item is True]
        else:
            if not callable(self.__func):
                type_name = type(self.__func).__name__
                raise TypeError(f"'{type_name}' object is not callable")
            self.__result = [i for i in self.__data if self.__func(i) is True]

    def __iter__(self):
        if not self.__result:
            self.__filter()

        for item in self.__result:
            yield item


def main():
    """'main'
    tests for ft_filter
    """
    test1 = "2string filtered1"
    # not_iterable = ft_filter(lambda x: x.isdigit(), 1)
    # not_callable = ft_filter(1, test1)
    # not_callable_list = list(not_callable)
    doc_filter = filter.__doc__
    doc_ft_filter = ft_filter.__doc__
    print(f"__doc__ is same: {doc_filter == doc_ft_filter}")

    filtered = filter(lambda x: x.isdigit(), test1)
    print(f"filter: {filtered}, {list(filtered)}")
    ft_filtered = ft_filter(lambda x: x.isdigit(), test1)
    print(f"ft_filter: {ft_filtered}, {list(ft_filtered)}")


if __name__ == "__main__":
    main()
