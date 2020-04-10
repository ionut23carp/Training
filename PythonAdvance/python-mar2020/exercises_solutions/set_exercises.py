def count_common_elements(list1, list2):
    return len(set(list1) & set(list2))


print(count_common_elements([1, 1, 2, 3], [2, 3, 2, 2, 3, 4]))


def count_unique_words(text):
    words = text.split()
    return len(set(words))


print(count_unique_words('hello hello is there anybody in there'))
