d = {'times': 100,
     'name': 'George',
     'hobbies': ['fishing', 'hiking']}

d['friends'] = ['Andrei', 'Mihai', 'Alina']
d['friends'].sort()
d['hobbies'].remove('hiking')
del d['times']
print(d)


def number_of_occurrences(words):
    occurrences = {}
    for word in set(words):
        occurrences[word] = words.count(word)
    return occurrences


print(number_of_occurrences(['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']))


def map_lists_v1(list1, list2):
    d = {}
    for index, elem in enumerate(list1):
        if len(list2) > index:
            d[elem] = list2[index]
    return d


def map_lists_v2(list1, list2):
    d = {}
    min_length = min(len(list1), len(list2))
    for idx in range(min_length):
        d[list1[idx]] = list2[idx]
    return d


print(map_lists_v1([1, 2, 3, 4], ['Ana', 'Vali', 'Geo']))
print(map_lists_v2([1, 2, 3, 4], ['Ana', 'Vali', 'Geo']))
