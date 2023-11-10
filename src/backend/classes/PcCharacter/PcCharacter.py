import math

from src.backend.classes.utils.die import Die
from src.backend.classes.utils.utils import get_class_features, clean_lower, clean_upper


class PcCharacter:
    """
    Class to store all the character data and manipulate it. By default, it creates a character at level 1 and then
    according to the experience it gained it will ask the user to level the character up
    """

    def __init__(self, name: str = "",
                 _class: str = "",
                 race: str = "",
                 background: str = "",
                 alignment: str = "",
                 movement_speed: int = 30,
                 xp=0,
                 stats: dict = None,
                 level: int = None,
                 *args,
                 **kwargs) -> None:
        """
        Initialize the character, creates the character at level 1 as stated in the PHB rules
        """
        self.name = name
        self.race = race
        self.background = background
        self.alignment = alignment
        self.xp = xp
        self.MS = movement_speed
        self.max_hp = 0
        self._prof_bonus = 2
        self.level = level if level else 1

        """Stats section"""
        self.stats = {
            "STR": {
                "mod": self._stat_mod(stats["STR"]),
                "score": stats["STR"]
            },
            "DEX": {
                "mod": self._stat_mod(stats["DEX"]),
                "score": stats["DEX"]
            },
            "CON": {
                "mod": self._stat_mod(stats["CON"]),
                "score": stats["CON"]
            },
            "INT": {
                "mod": self._stat_mod(stats["INT"]),
                "score": stats["INT"]
            },
            "WIS": {
                "mod": self._stat_mod(stats["WIS"]),
                "score": stats["WIS"]
            },
            "CHA": {
                "mod": self._stat_mod(stats["CHA"]),
                "score": stats["CHA"]
            }
        }
        self.AC = 10 + self.DEX
        self._skills = SkillManager()

        # Get basic class features
        self.features = get_class_features(_class, 0)
        self._hit_die = self.features["hit_die"]
        self._saving_throws = self.features["saving_throws"]
        self._proficiencies = self.features["proficiencies"]
        self._hit_die_faces = Die.get_faces(self._hit_die)
        self.init_features()

        # After initializing features
        self.update_features()

        """Turn-based section"""
        self._actions = [
            AttackAction()
        ]
        self._bonus_actions = []
        self._reaction = []

    def init_features(self):
        self.update_hp()
        self._update_prof_bonus()

    def update_features(self):
        self.features = get_class_features(self._class, self.level)

    def update_hp(self, take_average=True):
        """By default use averages"""
        if self._level == 1:
            self.max_hp = self._hit_die_faces + self.CON
        else:
            if take_average:
                self.max_hp += (self._hit_die_faces // 2 + 1) + self.CON
            else:
                self.max_hp += Die.roll(self._hit_die) + self.CON

    @classmethod
    def _stat_mod(cls, stat: int = 0):
        """Returns the modifier of a stat value"""
        return (stat - 10) // 2

    def _update_prof_bonus(self):
        """Calculate proficiency bonus at current level"""
        if self.prof_bonus:
            self.prof_bonus = math.ceil(1 + 1 / 4 * self._level)
        else:
            return math.ceil(1 + 1 / 4 * self._level)

    def roll_saving_throw(self, ability: str):
        ability = clean_upper(upper)
        roll = Die.roll20()
        if ability in self._saving_throws:
            roll += self._prof_bonus
        return roll

    def roll_check(self, skill: str):
        skill = clean_lower(skill)
        return self._skills.roll_skill(skill, self.stats)


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
    print(My_Pc._prof_bonus + My_Pc.STR)
