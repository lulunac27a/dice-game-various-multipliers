import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import random

def dice_game(num_rolls = 10, num_players = 2, highest_guess = 4, guess = 7):
    scores = [0] * num_players
    score_multiplier = 1
    score_multiplier_for_doubles = 1
    score_multiplier_for_sixes = 1
    score_multiplier_for_highest_guess = 1
    score_multiplier_for_sequential = 1
    score_multiplier_for_close_dice = 1
    score_multiplier_for_low_or_high = 1
    for i in range(num_rolls):
        for player in range(num_players):
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            total_rolls = roll1 + roll2
            double_roll = roll1 == roll2
            if double_roll:
                score_multiplier_for_doubles *= 2
            else:
                score_multiplier_for_doubles = 1
            
            if roll1 == 6 or roll2 == 6:
                score_multiplier_for_sixes *= 2
            else:
                score_multiplier_for_sixes = 1
            
            if max(roll1, roll2) == highest_guess:
                score_multiplier_for_highest_guess *= 2
            else:
                score_multiplier_for_highest_guess = 1
            
            if roll2 >= roll1:
                score_multiplier_for_sequential *= 2
            else:
                score_multiplier_for_sequential = 1
            
            diff = abs(roll1 - roll2)
            if diff == 1 or diff == 0:
                score_multiplier_for_close_dice *= 2
            else:
                score_multiplier_for_close_dice = 1
            
            if total_rolls == guess:
                score_multiplier *= 2
            else:
                score_multiplier = 1
            
            if total_rolls == 2 or total_rolls == 3 or total_rolls == 11 or total_rolls == 12:
                score_multiplier_for_low_or_high *= 2
            else:
                score_multiplier_for_low_or_high = 1
            
            score_multiplier_for_two_sixes = 2 if roll1 == 6 and roll2 == 6 else 1
            scores[player] += (roll1 + roll2) * score_multiplier * score_multiplier_for_doubles * score_multiplier_for_sixes * score_multiplier_for_two_sixes * score_multiplier_for_highest_guess * score_multiplier_for_sequential * score_multiplier_for_close_dice * score_multiplier_for_low_or_high

    return scores

num_rolls_slider = widgets.IntSlider(
    value=10,
    min=1,
    max=20,
    step=1,
    description='Rolls:',
    continuous_update=False)

num_players_slider = widgets.IntSlider(
    value=2,
    min=1,
    max=10,
    step=1,
    description='Players:',
    continuous_update=False)

change_value = widgets.Button(description='Roll Dice')
output = widgets.Output()

display(num_rolls_slider, num_players_slider, change_value, output)

def roll_dice(change):
    with output:
        clear_output()
        global numRolls, numPlayers
        scores = dice_game(num_rolls_slider.value, num_players_slider.value)
        print(scores)
        return scores
        
change_value.on_click(roll_dice)

num_rolls_slider.observe(roll_dice, names='rolls')
num_players_slider.observe(roll_dice, names='players')
rolls = num_rolls_slider.value
players = num_players_slider.value