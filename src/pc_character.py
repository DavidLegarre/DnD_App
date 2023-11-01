class PC:
    """
    PC (Playable Character) Class to manipulate and organize
    """
    def __init__(self, name: str, classes: list[str]):
        self._name = name
        if isinstance(classes, list):
            self._classes = classes
        else:
            self._classes.append(classes)
