import random
from typing import Iterable

def create(cand: Iterable, num: int):
    return ''.join([random.choice(cand) for i in range(num)])

cand = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f')

print(create(cand, 64))
