#V1:
cards = ["jack", "queen", "king"]

def main():
    print(random.choices(cards, weights=[75, 20,5], k=2))

main()


#V2:
import random 

cards = ["jack", "queen", "king"]

def main():
    print(random.sample(cards, k=2))

main()