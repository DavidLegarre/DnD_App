class Feature:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def apply(self, character):
        raise NotImplementedError("Apply method must be implemented in subclasses")