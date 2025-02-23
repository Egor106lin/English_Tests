import base64
import json

import unittest

def from_cookie_to_dict(cookie_value: str) -> dict:
    '''Эта функция шифрует куку.'''
    cookie_value_as_jsonstring = base64.b64decode(cookie_value).decode()
    cookie_value_dictionary = json.loads(cookie_value_as_jsonstring)
    return cookie_value_dictionary


def from_dict_to_cookie(cookie_value_dictionary: dict) -> str:
    '''Эта функция расшифровывает куку.'''
    cookie_value_as_json = json.dumps(cookie_value_dictionary)
    cookie_value_as_jsonstring = cookie_value_as_json.encode()
    cookie_value = base64.b64encode(cookie_value_as_jsonstring).decode()
    return cookie_value


class TestCookieFunctions(unittest.TestCase):

    def test_dict_to_str(self):
        dict = {"count": 1, "state": "end"}
        result = from_dict_to_cookie(dict)
        self.assertEqual(result, 'eyJjb3VudCI6IDEsICJzdGF0ZSI6ICJlbmQifQ==')
        
    def test_str_to_dict(self):
        string = 'eyJjb3VudCI6IDEsICJzdGF0ZSI6ICJlbmQifQ=='
        result = from_cookie_to_dict(string)
        self.assertEqual(result, {"count": 1, "state": "end"})

if __name__ == '__main__':
    unittest.main()
    