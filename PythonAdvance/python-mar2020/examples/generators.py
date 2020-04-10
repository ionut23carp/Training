def gen_numbers():
    num = 0
    print('Before first yield')
    yield num
    num += 1
    print('Before second yield')
    yield num
    num += 1
    print('Before last yield')
    yield num
    print('After last yield')


it = gen_numbers()
print(it)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # this would raise StopIteration


def stepper(n):
    ret = 0
    while ret < n:
        yield ret
        ret += 1


for nr in stepper(5):
    print(nr)
