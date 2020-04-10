import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print()
        print('Func is decorated!')
        print('Function arguments:', args, kwargs)
        return_value = func(*args, **kwargs)
        print('After decoration')
        return return_value

    return wrapper


# say_hello = decorator(say_hello)


@decorator
def say_hello():
    print('Hello world!')


@decorator
def say_bye():
    print('Good bye!')


@decorator
def greet(name):
    print(f'Hello, {name}!')


@decorator
def two_number_diff(a, b):
    return a - b


@decorator
def two_number_something(a, b, flag=True):
    if flag:
        return a - b
    else:
        return a + b


say_hello()
say_bye()

greet('Ana')
result = two_number_diff(10, 2)
print('Result', result)

result = two_number_something(10, 2, flag=False)
print('Result', result)


def multiply(nr):
    def inner_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return nr * func(*args, **kwargs)
        return wrapper
    return inner_func


@multiply(2)
def two_number_diff(a, b):
    return a - b


@multiply(3)
def two_number_sum(a, b):
    return a + b


# two_number_diff = multiply(2)(two_number_diff)
# two_number_diff = inner_func(two_number_diff)
# two_number_diff(*args, **kwargs) = wrapper(*args, **kwargs)

doubled_result = two_number_diff(10, 2)
print(doubled_result)

tripled_result = two_number_sum(10, 2)
print(tripled_result)

tripled_result = two_number_sum(1, 5)
print(tripled_result)
