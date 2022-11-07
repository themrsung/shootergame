from weapon import *

class Glock(Weapon):
    def __init__(self):
        super.__init__(WeaponData(
            10,
            20,
            120,
            120,
            0
        ))