class PC:
    """
    PC (Playable Character) Class to manipulate and organize
    """
    def __init__(self, name: str, classes: List[str]):
        self.name = name
        if isinstance(classes, list):
            self.classes = classes
        else:
            self._classes.append(classes)

    def __repr__(self):
        return f"Name: {self.name}\nClasses: {self.classes}"
