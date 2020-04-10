import unittest
from unittest.mock import patch


def get_words_from_file(file):
    words = []
    with open(file) as f:
        for line in f:
            words.extend(line.split())
    return words


def filter_long_words(*words, file_input=None, min_length=0):
    if file_input:
        words = get_words_from_file(file_input)

    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


class FilterLongWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.words_list = ['hello', 'bye', 'hi']

    def test_no_arguments(self):
        actual_result = filter_long_words()
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_words_not_null_min_length(self):
        actual_result = filter_long_words(*self.words_list, min_length=2)
        expected_result = ['hello', 'bye']
        self.assertEqual(actual_result, expected_result)

    def test_words_min_length_bigger_than_max_word_length(self):
        actual_result = filter_long_words(*self.words_list, min_length=10)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_integers_raise_error(self):
        with self.assertRaises(TypeError):
            filter_long_words(1, 2, 3)

    @patch('test_filter_long_words.get_words_from_file')
    def test_file_input(self, get_words_from_file_mock):
        filename = 'my_text.txt'
        get_words_from_file_mock.return_value = ['hello', 'world', 'x', 'y']
        actual_result = filter_long_words(file_input=filename, min_length=2)
        expected_result = ['hello', 'world']
        self.assertEqual(actual_result, expected_result)
        get_words_from_file_mock.assert_called_once_with(filename)


if __name__ == '__main__':
    unittest.main()
