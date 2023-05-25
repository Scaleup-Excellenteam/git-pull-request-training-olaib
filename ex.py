from functools import wraps


def type_check(expected_type):
    """
    this is a decorator that checks the type of the argument
    :param expected_type: the expected type of the argument
    :return: the function if the type is as expected
    :raises AssertionError: if the type is not as expected
    """

    def decorator(func):
        """
        this is the decorator that will be returned
        :param func: the function to check the type of the argument
        :return: the result of the function if the type is as expected
        """

        @wraps(func)
        def wrapper(arg):
            assert isinstance(arg, expected_type), f'Expected {expected_type} but got {type(arg)}'
            return func(arg)

        # return the wrapper function
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    """
    in this example we use the decorator to check the type of the argument
    was as expected(int)
    :param num: num to check and if it's int multiply by 2
    :return: num * 2
    """
    return num * 2


# ======================== OPTIONAL ========================
def execute_twice(func):
    """
        this is the decorator that will be returned
        :param func: the function to execute twice
        :return: the result of the function executed twice | None if the function is void
    """

    @wraps(func)
    def wrapper(*args):
        for i in range(2):
            func(*args)

    return wrapper


@execute_twice
def print_twice():
    """
    this function will be executed twice
    :return: None
    """
    print('hello world')


# ======================== SURPRISE ========================


def surprise(func):
    """
    this is the decorator that will be returned
    :param func: the function to execute twice
    :return: the result of the function executed twice | None if the function is void
    """

    @wraps(func)
    def wrapper(*args):
        print('surprise!')

    return wrapper


@surprise
def original_func():
    print('original func')


if __name__ == '__main__':
    print(times2(2))
    print_twice()
    original_func()
    print(times2('blah blah blah'))
