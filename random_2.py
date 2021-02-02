import random


class Dice:
    def roll(self):
        first = random.randint(1,9)
        second = random.randint(1,9)
        return first, second


dice = Dice()
print(dice.roll())
 




