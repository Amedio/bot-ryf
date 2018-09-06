from random import randint

def roll_simple():
    return

def roll_bonus(mod, difficulty=0):
    return

def dices(dicevalue=10,amount=3):
    min = 1
    max = dicevalue

    result = []

    for _ in range(amount):
        result.append(randint(min, max))

    return result