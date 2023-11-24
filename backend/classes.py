class CharacterRequest:
    character_id: str

    def __repr__(self) -> str:
        return f"Character id: {self.character_id}"
