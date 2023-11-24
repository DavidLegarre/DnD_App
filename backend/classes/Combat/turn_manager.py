from src.backend.classes.PcCharacter.PcCharacter import PcCharacter


class TurnManager:
    def __init__(self, participants: list[PcCharacter]):
        self.participants = participants

    def turn(self):
        for participant in self.participants:
            participant.get_action()
            participant.get_bonus_action()
            participant.get_reaction()

