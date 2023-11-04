import math

from src.backend.classes.die import die_calculator
from utils.utils import get_class_features


class PcCharacter:
    """
    """

    def __init__(self, name,
                 _class,
                 race, background,
                 alignment, movement_speed=30,
                 XP=0,
                 stats: dict = None) -> None:
        """
        Class to store all the character data and manipulate it. By default, it creates a character at level 1 and then
        according to the experience it gained it will ask the user to level the character up
        """

        self.name = name
        self.race = race
        self.background = background
        self.alignment = alignment
        self.XP = XP
        self.die = die_calculator()  # Die utility
        self.MS = movement_speed

        for stat, value in stats.items():
            mod_value = self._stat_mod(value)
            setattr(self, stat, mod_value)
            setattr(self, stat + "_score", value)

        level_0_features = get_class_features(_class, 0)
        self._hit_die = level_0_features["hit_die"]
        self._hit_die_faces = self.die.get_faces(self._hit_die)
        print(level_0_features)
        self._level = 1
        self.init_features()

    def init_features(self):
        self.calculate_hp()
        self._prof_bonus()

    def calculate_hp(self, take_average=True):
        """By default use averages"""
        if self._level == 1:
            self.max_hp = self._hit_die_faces + self.CON
        else:
            if take_average:
                self.max_hp += (self._hit_die_faces // 2 + 1) + self.CON

    def _stat_mod(self, stat: int = 0):
        """Returns the modifier of a stat value"""
        return (stat - 10) // 2

    def _prof_bonus(self):
        """Calculate proficiency bonus at current level"""
        self._bonus = math.ceil(1 + 1 / 4 * self._level)


if __name__ == '__main__':
    stats = {
        "STR": 20,
        "DEX": 20,
        "CON": 20,
        "INT": 20,
        "WIS": 20,
        "CHA": 20
    }
    My_Pc = PcCharacter(
        name="Lalkish Test", _class="Barbarian",
        race="", background="", alignment="", stats=stats
    )

    print(My_Pc._hit_die)
    print(My_Pc.max_hp)
    print(My_Pc._prof_bonus() + My_Pc.STR)
