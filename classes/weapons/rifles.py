from weapon import *

class Armalite(Weapon):
    def __init__(self):
        super.__init__(WeaponData(
            25,
            16,
            270,
            270,
            0
        ))