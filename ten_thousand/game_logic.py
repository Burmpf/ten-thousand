from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def validate_keepers(dice_roll, dice_kept):
        dice_roll_validation = Counter(dice_roll)
        dice_kept_validation = Counter(dice_kept)

        if len(dice_kept_validation) <= len(dice_roll_validation):
            if all(dice_kept_validation[key] <= dice_roll_validation[key] for key in dice_kept_validation.keys()):
                return True
            return False
        else:
            return False

    @staticmethod
    def roll_dice(num_dice):

        return tuple(randint(1, 6) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(roll_tuple):


        total_score = 0
        counted_dice = Counter(roll_tuple).most_common()

        if not counted_dice:
            return total_score

        # 3, 4, 5, and 6 of a kind
        if (counted_dice[0][1]) >= 3:
            if counted_dice[0][0] != 1:
                total_score += counted_dice[0][0] * 100 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total_score
                counted_dice = counted_dice[1:]
            else:
                total_score += 1000 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total_score
                counted_dice = counted_dice[1:]


            # Two 3 of a kinds
            if len(counted_dice) == 1:
                if counted_dice[0][1] == 3:
                    if counted_dice[0][0] != 1:
                        total_score += counted_dice[0][0] * 100
                        return total_score
                    else:
                        total_score += 1000
                        return total_score

        # Straight
        if len(counted_dice) == 6:
            if counted_dice[0][1] == 1:
                total_score += 1500
                return total_score


        # Three Pairs
        if len(counted_dice) == 3:
            if counted_dice[2][1] == 2:
                total_score += 1500
                return total_score


        # Single 5 or Single 1
        else:
            for dice in counted_dice:
                if dice[0] == 5:
                    total_score += dice[1] * 50
            for dice in counted_dice:
                if dice[0] == 1:
                    total_score += dice[1] * 100

        print("Total Score", total_score)
        return total_score

#roll simulates roll tests are making
#roll = roll_dice(6)
