from src.backend.classes.PcCharacter.PcCharacter import PcCharacter
from src.backend.classes.utils.die import Die


class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def perform(self, actor: PcCharacter):
        raise NotImplementedError("Perform method on base action class")


class AttackAction(Action):
    def __init__(self):
        super().__init__("Attack", "Perform a Melee or Ranged attack")

    def perform(self, actor: PcCharacter):
        print("Rolling for attack")
        r20 = Die.roll20()
        if actor.attack_weapon.melee:
            if actor.attack_weapon.finesse:
                bonus = actor.DEX
                total = r20+bonus+actor.prof_bonus
                print(f"Attack roll: {total} = {r20} + {bonus} + {actor.prof_bonus}")
                return total
            else:
                bonus = actor.STR
                total = r20 + bonus + actor.prof_bonus
                print(f"Attack roll: {total} = {r20} + {bonus} + {actor.prof_bonus}")
                return total
        else:
            bonus = actor.DEX
            total = r20 + bonus + actor.prof_bonus
            print(f"Attack roll: {total} = {r20} + {bonus} + {actor.prof_bonus}")
            return total
