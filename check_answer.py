import unittest

from exercises import *


def check_answer(question: int, answer: str, answers: dict, exerscices: list[dict[list]]) -> bool:
    '''This function gets question number, user answer, dictionary with correct answers,
    and dictionary with user list of questions. Return True if answer is correct.'''
    answer_to_check = next(iter(exerscices[question]))
    return answers[answer_to_check] == answer
    

class TestCookieFunctions(unittest.TestCase):

    def test_check_answer_correct_answer_(self):
        question = 1
        answer = 'will visit'
        answers = answers_english_tenses_test
        exerscices = english_tenses_test_original
        result = check_answer(question, answer, answers, exerscices)
        self.assertTrue(result)

    def test_check_answer_incorrect_answer_(self):
        question = 1
        answer = 'visited'
        answers = answers_english_tenses_test
        exerscices = english_tenses_test_original
        result = check_answer(question, answer, answers, exerscices)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
    