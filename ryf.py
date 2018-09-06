from random import randint

def roll(dice_index):
    result = []

    all_rolls = []
    roll_result = dices()
    all_rolls.append(roll_result)

    objective = sorted(roll_result)[dice_index]

    if objective == 1:
        if dice_index < 2:
            next_dice = sorted(roll_result)[dice_index + 1]
            if next_dice <= 5:
                result.append(all_rolls)
                result.append(objective)
                result.append(next_dice)
                return result
        else:
            result.append(all_rolls)
            result.append(objective)
            return result
    
    total_roll = objective

    while objective == 10:
        roll_result = dices()
        all_rolls.append(roll_result)
        objective = sorted(roll_result)[dice_index]

        total_roll = total_roll + objective
    
    result.append(all_rolls)
    result.append(total_roll)

    return result

def dices(dicevalue=10, amount=3):
    min = 1
    max = dicevalue

    result = []

    for _ in range(amount):
        result.append(randint(min, max))

    return result