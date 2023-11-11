from src.backend.classes.PcCharacter.PcCharacter import PcCharacter


class Equipment:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class Armor(Equipment):
    def __init__(self, name: str, type: str, ac: int):
        super().__init__(name, type)
        self.ac = ac

    def equip(self, actor: PcCharacter):
        actor.ac = self.ac
