from copy import deepcopy
import random

from exercises import *
import unittest


def create_random_words_for_user(seed: int, words: list[dict[list]]) -> list[dict[list]]:
    '''Эта фукнция перемешивает оригинальный список заданий и возвращает перемешанный вариант для пользователя.'''
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
        words_test = english_tenses_test_original
        result = create_random_words_for_user(seed, words_test)
        self.assertEqual(len(english_tenses_test_original), len(result))
        self.assertEqual(result[2], {'It ___ you a lot of energy.': ['gives', 'gave', 'will give', 'give']})

if __name__ == '__main__':
    unittest.main()
