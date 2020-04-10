import random


def gen_random(max_nr):
    while True:
        yield random.randint(1, max_nr)


print('Generate 10 random numbers between 1 and 5:')

it = gen_random(5)
for i in range(10):
    print(next(it))

print('\nGenerate 5 more random numbers between 1 and 5:')

i = 0
for random_nr in it:
    print(random_nr)
    i += 1
    if i == 5:
        break


def gen_unique_v1(seq):
    unique_elems = []
    for i in seq:
        if i in unique_elems:
            continue
        unique_elems.append(i)
        yield i


def gen_unique_v2(seq):
    for i in set(seq):
        yield i


print('\nGenerate unique elements from list:')
for elem in gen_unique_v1([1, 1, 1, 3, 5, 6, 3, 3, 5]):
    print(elem)

print('\nGenerate unique elements from string:')
for elem in gen_unique_v2("absbabasa"):
    print(elem)
