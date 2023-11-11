import src.backend.classes.PcCharacter as PcCharacter
from src.backend.classes.utils.die import Die


class Action:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @staticmethod
    def perform(actor: PcCharacter):
        raise NotImplementedError("Perform method on base action class")


class AttackAction(Action):
    def __init__(self):
        super().__init__("Attack", "Perform a Melee or Ranged attack")

    @staticmethod
    def perform(actor: PcCharacter):
        print("Rolling for attack")
        r20 = Die.roll20()
        bonus_str = actor.STR
        total_str = r20 + bonus_str + actor.prof_bonus
        bonus_dex = actor.DEX
        total_dex = r20 + bonus_dex + actor.prof_bonus

        if actor.attack_weapon is None:
            print(f"Attack roll: {total_str} = {r20} + {bonus_dex} + {actor.prof_bonus}")
            return total_str
        if actor.attack_weapon.melee:
            if actor.attack_weapon.finesse:
                print(f"Attack roll: {total_dex} = {r20} + {bonus_dex} + {actor.prof_bonus}")
                return total_dex
            else:
                print(f"Attack roll: {total_str} = {r20} + {bonus_str} + {actor.prof_bonus}")
                return total_str
        else:
            print(f"Attack roll: {total_dex} = {r20} + {bonus_dex} + {actor.prof_bonus}")
            return total_dex
