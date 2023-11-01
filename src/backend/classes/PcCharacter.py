from utils.utils import get_class_features


class PcCharacter():
    """
    """

    def __init__(self, name,
                 _class, level,
                 race, background,
                 alignment, XP=0,
                 stats: dict = None) -> None:

        self.name = name
        self._stats = stats
        level_0_features = get_class_features(_class, 0)
        hit_die = level_0_features["hit_die"]
        print(level_0_features)
        self.level = level

    def init_features(self, features):
        self.calculate_hp()
        pass

    def caculate_hp(self,):
        """By default use averages"""
        pass


if __name__ == '__main__':
    stats = {
        "STR": 20,
        "DEX": 20,
        "CON": 20,
        "INT": 20,
        "WIS": 20,
        "CHA": 20
    }
    My_Pc = PcCharacter(
        name="Lalkish Test", Class="Barbarian",
        level=1, race="", background="", alignment="", stats=stats
    )
