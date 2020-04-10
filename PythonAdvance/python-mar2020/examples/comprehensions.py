multiples_of_3 = []
for nr in range(10):
    if nr % 2 == 0:
        multiples_of_3.append(nr * 3)
print(multiples_of_3)


multiples_of_3_comprehension = [nr * 3 for nr in range(10) if nr % 2 == 0]
print(multiples_of_3_comprehension)

words = ['bye', 'hello', 'hi', 'world']
word_lengths = [(word, len(word)) for word in words]
print(word_lengths)


word_length_dict = {word: len(word) for word in words if word.startswith('h')}
print(word_length_dict)

word_length_dict_multiply = {word.upper(): word_length * 10 for word, word_length in word_length_dict.items()}
print(word_length_dict_multiply)


l = [1, 1, 1, 3, 4, 3, 4, 2]
unique_numbers_div_by_2 = {elem for elem in l if elem % 2 == 0}
print(unique_numbers_div_by_2)


m = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
l1 = [[row[i] for row in m] for i in range(3)]
print(l1)
