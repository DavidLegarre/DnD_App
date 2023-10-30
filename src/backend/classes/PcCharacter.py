from backend.classes.utils.utils import get_class_features


class PcCharacter():
    """
    """

    def __init__(self, name,
                 Class, level,
                 race, background,
                 alignment, XP=0,
                 stats: list = None) -> None:

        self.name = name
        self._stats = stats
        level_0_features = get_class_features(Class, 0)
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
    My_Pc = PcCharacter(
        name="Lalkish Test", Class="Barbarian",
        level=1, race="", background="", alignment=""
    )
