"""
Dice game with various score multipliers by addition.
"""

import random  # generate random numbers


def dice_game(num_rolls=10, num_players=2, highest_guess=4, guess=7):
    """
    Dice game with various score multipliers that multiply by 2 if criteria meets the requirements, else reset to 1.
    """
    scores = [0] * num_players  # set score to 0 for specified number of players
    score_multiplier = 1  # set score multiplier to 1
    score_multiplier_for_doubles = 1  # set score multiplier for doubles to 1
    score_multiplier_for_sixes = 1  # set score multiplier for sixes to 1
    score_multiplier_for_highest_guess = (
        1  # set score multiplier for highest guess to 1
    )
    score_multiplier_for_sequential = 1  # set score multiplier for sequenial dice to 1
    score_multiplier_for_close_dice = 1  # set score multiplier for close dice to 1
    score_multiplier_for_low_or_high = (
        1  # set score multipler for low or high dice to 1
    )
    for _ in range(num_rolls):  # repeat for each roll
        for player in range(num_players):  # repeat for each player
            roll1 = random.randint(1, 6)  # set first rolled dice to 1 to 6
            roll2 = random.randint(1, 6)  # set second rolled dice to 1 to 6
            total_rolls = (
                roll1 + roll2
            )  # set total rolls to sum of first and second rolls
            double_roll = (
                roll1 == roll2
            )  # check for doubles (first rolled dice is equal to second rolled dice)
            if double_roll:  # if roll is double
                score_multiplier_for_doubles += 1  # increase score multiplier by 1
            else:
                score_multiplier_for_doubles = 1  # reset score multiplier to 1

            if roll1 == 6 or roll2 == 6:  # if rolled dice has a six
                score_multiplier_for_sixes += 1
            else:
                score_multiplier_for_sixes = 1

            if (
                max(roll1, roll2) == highest_guess
            ):  # if highest dice rolled is equal to highest guess value
                score_multiplier_for_highest_guess += 1
            else:
                score_multiplier_for_highest_guess = 1

            if (
                roll2 >= roll1
            ):  # if second rolled dice is greater than or equal to first rolled dice
                score_multiplier_for_sequential += 1
            else:
                score_multiplier_for_sequential = 1

            diff = abs(
                roll1 - roll2
            )  # calculate difference between first rolled dice and second rolled dice
            if diff == 1 or diff == 0:  # if difference is 0 or 1
                score_multiplier_for_close_dice += 1
            else:
                score_multiplier_for_close_dice = 1

            if total_rolls == guess:  # if sum of rolled dice is equal to guessed number
                score_multiplier += 1
            else:
                score_multiplier = 1

            if (
                total_rolls == 2
                or total_rolls == 3
                or total_rolls == 11
                or total_rolls == 12
            ):  # if total sum of rolled dice is 2, 3, 11, or 12
                score_multiplier_for_low_or_high += 1
            else:
                score_multiplier_for_low_or_high = 1

            score_multiplier_for_two_sixes = (
                2 if roll1 == 6 and roll2 == 6 else 1
            )  # if two rolled dice are both 6 double the score
            scores[player] += (
                (roll1 + roll2)
                * score_multiplier
                * score_multiplier_for_doubles
                * score_multiplier_for_sixes
                * score_multiplier_for_two_sixes
                * score_multiplier_for_highest_guess
                * score_multiplier_for_sequential
                * score_multiplier_for_close_dice
                * score_multiplier_for_low_or_high
            )  # add score from various score multipliers

    return scores  # return list of scores for all players


rolls = input("Number of rolls: ")  # set number of rolls based on input value
players = input("Number of players: ")  # set number of players based on input value
print(
    dice_game(rolls, players)
)  # print dice game result with specified number of rolls and number of players
