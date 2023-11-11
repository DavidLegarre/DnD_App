class Barbarian:
    def __init__(self):
        self.raging = False
        self.rage_count = 0
        self.raging_limit = 2
        self.rage_dmg = 2

    def enter_rage(self):
        self.rage_count += 1
        if self.rage_count > self.raging_limit:
            print("Rage limit reached, you must finish a long rest")
        elif self.raging:
            print("You're already in rage")
        else:
            self.raging = True

    def end_rage(self):
        if self.raging:
            self.raging = False
            print("Rage ended")
        else:
            print("You're not in rage")

    # TODO: Rethink this part
    def attack(self):
        if self.raging:
            print("Applying rage damage to the attack")
