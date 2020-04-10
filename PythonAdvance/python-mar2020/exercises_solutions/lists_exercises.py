# 1
letters = ['h', 'e', 'l', 'l', 'o']
text = ''.join(letters)
print(text)


# 2
def filter_long_words(words, min_length):
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


# 3
def have_common_element(list1, list2):
    # 2 for-uri
    # 1 for + in operator
    for elem in list1:
        if elem in list2:
            return True
    return False


# 4
numbers = [1, 1, 1, 2, 2, 3, 4, 5, 5]
unique_numbers = []
for nr in numbers:
    if nr not in unique_numbers:
        unique_numbers.append(nr)
print(len(unique_numbers))

numbers = [1, 1, 1, 2, 2, 3, 4, 5, 5]
count = 1
for idx in range(1, len(numbers)):
    if numbers[idx-1] != numbers[idx]:
        count += 1
print(count)
