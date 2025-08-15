#V1:
from random import choice 

coin = choice(["heads", "tails"])
print(coin)

#V2:
import random

number = random.randint(1, 10)
print(number)

#V3:
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(cards)

#V4:
