import yaml

from src.backend.classes.PcCharacter.features.Feature import Feature

with open('features_data.yaml', 'r') as file:
    descriptions = yaml.safe_load(file)

descriptions = descriptions["Barbarian"]


class Rage(Feature):
    def __init__(self):
        super().__init__("Rage", descriptions['rage'])


class UnarmoredDefense(Feature):
    def __init__(self):
        super().__init__("unarmored_defense", descriptions["unarmored_defense"])

    def apply(self, character):
        if character.armor is None:
            new_ac = 10 + character.DEX + character.CON
            character.update_AC(new_ac)
        else:
            print("Unarmored Defense doesn't apply while wearing armor")


if __name__ == '__main__':
    print(descriptions['rage'])
