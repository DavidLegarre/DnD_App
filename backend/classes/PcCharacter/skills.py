from src.backend.classes.utils.die import Die


class SkillManager():
    """
    Class to manage the skills, proficiencies and saving throws of a character
    """

    def __init__(self):
        self.skills = {
            "STR": ["athletics"],
            "DEX": ["acrobatics", "sleight_of_hand", "stealth"],
            "INT": ["arcana", "history", "investigation", "nature", "religion"],
            "WIS": ["animal_handling", "insight", "medicine", "perception", "survival"],
            "CHA": ["deception", "intimidation", "performance", "persuasion"]
        }
        self.die = Die()
        self.proficiencies = {}
        for ability, skill in self.skills.items():
            self.proficiencies[skill] = False

    def roll_skill(self, skill, stats, prof_bonus: int = None):
        bonus = self.get_bonus(stats, skill)
        roll = self.die.roll20() + bonus
        if self.proficiencies[skill]:
            roll += prof_bonus

        return roll

    def get_bonus(self, stats: dict, skill_to_roll: str):
        for ability, skill in self.skills.items():
            if skill_to_roll == skill:
                return stats[ability]
        raise ValueError(f"Couldn't find the bonus for skill: {skill_to_roll}")

