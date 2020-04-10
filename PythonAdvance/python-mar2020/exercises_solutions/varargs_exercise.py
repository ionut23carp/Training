def filter_long_words(*words, min_length=0):
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


def filter_long_words_v2(*words, **kwargs):
    # This is just to exemplify **kwargs
    # The version above is more suitable for this example
    min_length = kwargs.get('min_length', 0)
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


print(filter_long_words('hello', 'bye', 'hi'))
print(filter_long_words('hello', 'bye', 'hi', min_length=3))
