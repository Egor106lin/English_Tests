import random

words = [{1: 1}, {2: 2}, {3: 3}]
randomizer = random.Random(15648)
from copy import deepcopy
new_list = deepcopy(words)
randomizer.shuffle(new_list)
randomizer.shuffle(new_list)
print(new_list)
