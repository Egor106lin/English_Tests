from random import choice
from words_list import words

# Создаём список ключей словаря со словами
list_of_keys = []
for key in words.keys():
    list_of_keys.append(key)
context = {}
while len(list_of_keys) > 0:
    key = choice(list_of_keys)
    list_of_keys.remove(key)
    final_key = words.get(key)
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
    value = [english_word, translate1, translate2, translate3, translate4]
    context[english_word] = value