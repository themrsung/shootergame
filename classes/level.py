class Level:
    def __init__(self, pawns, weapons, projectiles):
        self.pawns = pawns
        self.weapons = weapons
        self.projectiles = projectiles
    
    def tick(self):
        for pawn in self.pawns:
            pawn.tick()

        for weapon in self.weapons:
            weapon.tick()
        
        for projectile in self.projectiles:
            projectile.tick()