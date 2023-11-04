import random
import re
import numpy as np


class die_calculator():
    def __init__(self) -> None:
        pass

    def calculate_expression(self, expression: str) -> bool | int:
        """
        Function to calculate a die expression, using the same
        syntax as https://dice.clockworkmod.com/ tool
        """
        assert type(expression) is str, "Expression must be a string"
        expression = expression.lower()

        # Check for normal roll
        if re.match(r'^d\d+$', expression):
            return self.roll_die(expression[1:])

        # Check for roll with advantage
        if re.match(r'^(d\d+) (>) (d\d+)$', expression):
            die = re.match(r'^d\d+', expression)[0]
            return self.roll_adv(die[1:])

        # Check for roll with disadvantage
        if re.match(r'^(d\d+) (<) (d\d+)$', expression):
            die = re.match(r'^d\d+', expression)[0][1:]
            return self.roll_adv(die)

        # Check for a dc check
        if re.match(r'^d\d+.[+-].\d.dc.\d+$', expression):
            die = re.match(r'^d\d+', expression)[0][1:]
            DC = re.search(r'dc.\d+', expression).group()
            DC = re.search(r'\d+', DC).group()
            roll = self.roll_die(die)
            return (roll, roll > int(DC))

    def roll_die(self, faces):
        if not isinstance(faces, int):
            faces = int(faces)
        assert faces > 2, "a die must have at least 2 faces"
        return random.randint(1, faces)

    def roll_adv(self, faces):
        return max(self.roll_die(faces), self.roll_die(faces))

    def roll_disadv(self, faces):
        return min(self.roll_die(faces), self.roll_die(faces))

    def get_avg(self, expression: str = None):
        """Get the average of a roll expression"""
        avgs = 0
        expression = expression.strip()
        matches = re.findall(r'(\d+)d(\d+)', expression)
        for match in matches:
            num_rolls, die_roll = [int(n) for n in match]
            avg = np.sum(range(die_roll+1))/die_roll
            avgs += avg*num_rolls

        return avgs

    def get_faces(self, expression):
        matches = re.findall(r'(\d+)d(\d+)', expression)[0]
        return int(matches[1])


if __name__ == '__main__':
    die = die_calculator()
    expressions = [
        "d20", "d20 > d20",
        "d20 + 6 DC 15",
        "d20 - 6 DC 15"
    ]

    hit_die = '2d12 3d6'

    print(die.get_avg(hit_die))
