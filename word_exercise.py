from copy import deepcopy
import random

from words_list import english_excercices_first_test
import unittest


def create_random_words_for_user(seed: int, words: list[dict[list]]) -> list[dict[list]]:
    '''This function gets list of words and mix it. Returns mixed list.'''
    mixed_list = deepcopy(words)
    randomizer = random.Random(seed)
    randomizer.shuffle(mixed_list)
    for w in mixed_list:
        for k, v in w.items():
            randomizer.shuffle(v)
    return mixed_list


class TestRandomizer(unittest.TestCase):

    def test_create_random_words_for_user(self):
        seed = 48499
        words_test = english_excercices_first_test
        result = create_random_words_for_user(seed, words_test)
        self.assertEqual(len(english_excercices_first_test), len(result))
        self.assertEqual(result[3], {'dictionary': ['развод', 'дикция', 'лист', 'словарь']})

if __name__ == '__main__':
    unittest.main()
