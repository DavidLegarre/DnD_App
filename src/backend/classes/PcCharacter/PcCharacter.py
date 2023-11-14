import json
import math
import uuid
from pathlib import Path

from src.backend.classes.PcCharacter.Barbarian import Barbarian
from src.backend.classes.PcCharacter.actions.Action import AttackAction
from src.backend.classes.PcCharacter.features.Feature import Feature
from src.backend.classes.utils.die import Die
from src.backend.classes.utils.utils import get_class_features, clean_lower, clean_upper

available_classes = {
    'Barbarian': Barbarian()
}


class PcCharacter:
    """
    Class to store all the character data and manipulate it. By default, it creates a character at level 1 and then
    according to the experience it gained it will ask the user to level the character up
    """

    def __init__(self, id: str = uuid.uuid4(), name: str = "",
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
        self.id = str(id)
        self.name = name
        self.race = race
        self.background = background
        self.alignment = alignment
        self.xp = xp
        self.ms = movement_speed
        self.attack_weapon = None
        self.max_hp = 0
        self.prof_bonus = 2
        self._class = available_classes[_class]
        self.level = level if level else 1

        """Stats section"""
        self.STR = self._stat_mod(stats["STR"])
        self.STR_score = stats["STR"]
        self.DEX = self._stat_mod(stats["DEX"])
        self.DEX_score = stats["DEX"]
        self.CON = self._stat_mod(stats["CON"])
        self.CON_score = stats["CON"]
        self.INT = self._stat_mod(stats["INT"])
        self.INT_score = stats["INT"]
        self.WIS = self._stat_mod(stats["WIS"])
        self.WIS_score = stats["WIS"]
        self.CHA = self._stat_mod(stats["CHA"])
        self.CHA_score = stats["CHA"]

        self.ac = 10 + self.DEX

        # Get basic class features
        self.features = get_class_features(self._class, 0)
        self._hit_die = self.features["hit_die"]
        self._saving_throws = self.features["saving_throws"]
        self._proficiencies = self.features["proficiencies"]
        self._hit_die_faces = Die.get_faces(self._hit_die)
        self.init_features()

        # After initializing features
        self.update_features()

        """Turn-based section"""
        self._actions = {'attack': AttackAction()}
        self._bonus_actions = {}
        self._reaction = {}

        """Features"""
        self.features = []

        """Equipment"""
        self.equipment = []  # General equipment
        self.weapon = None  # equipped weapon
        self.armor = None  # equipped armor

    """Update character"""

    def init_features(self):
        self.update_hp()
        self._update_prof_bonus()

    def update_features(self):
        self.features = get_class_features(self._class, self.level)

    def update_hp(self, take_average=True):
        """By default use averages"""
        if self.level == 1:
            self.max_hp = self._hit_die_faces + self.CON
        else:
            if take_average:
                self.max_hp += (self._hit_die_faces // 2 + 1) + self.CON
            else:
                self.max_hp += Die.roll(self._hit_die) + self.CON

    def _update_prof_bonus(self):
        """Calculate proficiency bonus at current level"""
        if self.prof_bonus:
            self.prof_bonus = math.ceil(1 + 1 / 4 * self.level)
        else:
            return math.ceil(1 + 1 / 4 * self.level)

    def _update_AC(self, new_ac):
        self.ac = new_ac

    """Utilities"""

    @staticmethod
    def _stat_mod(stat: int = 0):
        """Returns the modifier of a stat value"""
        return (stat - 10) // 2

    def roll_saving_throw(self, ability: str):
        ability = clean_upper(ability)
        roll = Die.roll20()
        if ability in self._saving_throws:
            roll += self.prof_bonus
        return roll

    def roll_check(self, skill: str):
        skill = clean_lower(skill)
        return self._skills.roll_skill(skill, self.stats)

    """Action methods"""

    def perform_action(self, action: str):
        action = action.lower()
        action = self._actions.get(action)
        if action:
            action.perform(self)
        else:
            raise KeyError(f"Unknown action {action}")

    """Features methods"""

    def add_feature(self, feature):
        if isinstance(feature, Feature):
            self.features.append(feature)
            feature.apply(self)

    """Turn methods"""

    def get_actions(self):
        output = {}
        for i, action in enumerate(self._actions):
            print(f"{i}: {action}")
        while True:
            try:
                player_action = int(input("Enter your selection: "))
                selected_action = list(self._actions.keys())[player_action]
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number")
        self._actions[selected_action].perform(self)

    def turn(self):
        self.get_actions()

    def convert_to_dict(self, obj):
        if isinstance(obj, dict):
            return {key: self.convert_to_dict(value) for key, value in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self.convert_to_dict(item) for item in obj]
        else:
            return obj

    def jsonify(self, path: Path):
        path = path / (self.id + ".json")
        result = {}
        for key, value in vars(self).items():
            if isinstance(value, dict):
                for _key, _value in value.items():
                    if isinstance(value, list) or isinstance(value, tuple):
                        continue
                    value[_key] = str(_value)
                result[key] = value
                continue
            result[key] = str(value)
        with open(path, "w") as f:
            json.dump(result, f)

        return result

    def save_character(self, path: Path):
        with open(path, 'a') as f:
            f.write(self.id + '\n')


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
        id="aa6d8217-60e7-441b-b589-269c27cade62",
        name="Lalkish Test", _class="Barbarian",
        race="", background="", alignment="", stats=stats
    )

    print(My_Pc._hit_die)
    print(My_Pc.max_hp)
    print(My_Pc.prof_bonus + My_Pc.STR)
    My_Pc.perform_action('attack')
    # My_Pc.turn()
    json_path = Path.cwd().parent.parent / 'data' / 'characters'
    pc_json = My_Pc.jsonify(json_path)
    json_path = json_path / 'database.txt'
    # My_Pc.save_character(json_path)
