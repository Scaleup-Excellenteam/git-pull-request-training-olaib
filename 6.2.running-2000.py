# running 2000
from timeit import timeit


def timer(func: callable, *args, **kwargs):
    return timeit(lambda: func(*args, **kwargs), number=1)


if __name__ == '__main__':
    print(timer(zip, range(1000000), range(1000000)))
