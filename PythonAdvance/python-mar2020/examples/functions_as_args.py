def two_number_sum(a, b):
    return a + b


def two_number_diff(a, b):
    return a - b


def get_result(a, b, operation):
    print(f'Function {operation.__name__} was called')
    return operation(a, b)


res = get_result(10, 2, two_number_sum)
print(res)

res = get_result(10, 2, two_number_diff)
print(res)

res = get_result(10, 2, lambda x, y: x*y)
print(res)

res = get_result(10, 2, lambda x, y: 0)
print(res)
