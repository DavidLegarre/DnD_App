import random
import re

import numpy as np


class Die():
    def __init__(self) -> None:
        pass

    @classmethod
    def roll20(cls):
        return cls.roll_die(20)

    @classmethod
    def calculate_expression(cls, expression: str) -> int | tuple[int, bool]:
        """
        Function to calculate a die expression, using the same
        syntax as https://dice.clockworkmod.com/ tool
        """
        assert type(expression) is str, "Expression must be a string"
        expression = expression.lower()
        die_regx = r'(\d+)d(\d+)'

        adv_dis_regx = r'(<|>)'
        dc_regx = r'(dc) (\d+)'
        bonus = r'(\+) (\d+)'

        if re.findall(r'^(d)(\d+)', expression):
            expression = '1' + expression

        dies = re.findall(die_regx, expression)

        adv_disv = re.findall(adv_dis_regx, expression)
        adv_disv = adv_disv[0] if adv_disv else False

        has_dc = int(re.findall(dc_regx, expression)[0][-1]) if re.findall(dc_regx, expression) else False

        if re.findall(bonus, expression):
            has_bonus = int(re.findall(bonus, expression)[0][-1]) * (-1 if bonus[0][0] == '-' else 1)
        else:
            has_bonus = False

        if dies is None:
            raise ValueError(f"No dice found in expression {expression}")

        roll = cls.roll_die(dies[0][-1], dies[0][0])

        if adv_disv:
            if adv_disv == '<':
                roll2 = cls.roll_die(dies[0][-1], dies[0][0])
                roll = min(roll, roll2)
            else:
                roll2 = cls.roll_die(dies[0][-1], dies[0][0])
                roll = max(roll, roll2)

        if has_bonus:
            roll += has_bonus

        if has_dc:
            return (roll, roll > has_dc)

        return roll

    @staticmethod
    def roll_die(faces: int, times: int = 1):
        faces = int(faces) if not isinstance(faces, int) else faces
        times = int(times) if not isinstance(times, int) else times
        assert faces > 2, "a die must have at least 2 faces"
        return sum([random.randint(1, faces) for _ in range(times)])

    @staticmethod
    def get_avg(expression: str = None):
        """Get the average of a roll expression"""
        avgs = 0
        expression = expression.strip()
        matches = re.findall(r'(\d+)d(\d+)', expression)
        for match in matches:
            num_rolls, die_roll = [int(n) for n in match]
            avg = np.sum(range(die_roll + 1)) / die_roll
            avgs += avg * num_rolls

        return avgs

    @staticmethod
    def get_faces(expression):
        matches = re.findall(r'(\d+)d(\d+)', expression)[0]
        return int(matches[1])


if __name__ == '__main__':
    expressions = [
        "d20", "d20 > d20",
        "d20 + 6 DC 15",
        "d20 - 6 DC 15",
        "3d6"
    ]

    for expression in expressions:
        print(Die.calculate_expression(expression))
