import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = func(*args, **kwargs)
        time_after = time.time()
        diff = time_after - time_before
        print(f'Execution took {diff:.5f}s')
        return result
    return wrapper


@timeit
def say_hello(name):
    return f'Hello, {name}'


@timeit
def slow_function():
    for i in range(2000):
        for j in range(5000):
            i * j


if __name__ == '__main__':
    print(say_hello('Ana'))
    slow_function()
