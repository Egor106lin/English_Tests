from random import choice
from words_list import words

from copy import deepcopy

local_words = deepcopy(words)

# Создаём список ключей словаря со словами
list_of_keys = []
for key in local_words.keys():
    list_of_keys.append(key)
context = {}
while len(list_of_keys) > 0:
    key = choice(list_of_keys)
    list_of_keys.remove(key)
    final_key = local_words.get(key)
    english_word = final_key[0]
    final_key.remove(final_key[0])
    choose = []
    a = choice(final_key)
    final_key.remove(a)
    b = choice(final_key)
    final_key.remove(b)
    c = choice(final_key)
    final_key.remove(c)
    d = choice(final_key)
    for i in [a, b, c, d]:
        choose.append(i)
    translate1, translate2, translate3, translate4 = choose[0], choose[1], choose[2], choose[3]
    value = [english_word, translate1, translate2, translate3, translate4, [english_word][1]]
    context[english_word] = value