# 1
products_eur = [
    ('branza', 5),
    ('paine', 1),
    ('cartofi', 0.5),
]

products_ron = map(lambda tup: (tup[0], tup[1]*4.75), products_eur)
print(list(products_ron))


# 2
def filter_short_words(word_list, n):
    return list(filter(lambda word: len(word) < n, word_list))


print(filter_short_words(['wdsczf', 'asd', 'aretfhj', 'afzez'], 6))


# 3
def order_by_occurrences(*words):
    return sorted(set(words), key=lambda word: words.count(word), reverse=True)


print(order_by_occurrences('hello', 'there', 'hello', 'hi', 'hi', 'hello'))
