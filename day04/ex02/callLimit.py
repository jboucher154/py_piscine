# from functools import wraps
# ->  fixes the name and doc string printouts for the wrapped function


def callLimit(limit: int):
    """callLimit, decorator

    Args:
        limit (int): limit of calls to function to be wrapped

    Returns:
        function : inner func that applies wrapper to function
    """
    count = 0

    def callLimiter(function):
        """callLimiter, decorator

        Args:
            function (_type_): function whose calls are to be  limited

        Returns:
            function: inner func that wraps decorated function
        """

        # @wraps(function) #from functools import wraps
        def limit_function(*args: any, **kwargs: any):
            """limit_function

            Returns:
                function: wrapped function with optional arguments
            Increments call counter and return function if limit not met
            or None if limit met.
            """
            nonlocal count
            if count >= limit:
                name = function.__name__
                loc = hex(id(function))
                print(f"Error: <function {name} at {loc}> call too many times")
                return None
            count += 1
            return function(*args, **kwargs)
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    # uncomment wraps imports and decorator application to see difference
    print(g.__name__)
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
