class Level:
    def __init__(self, objects):
        self.objects = objects
    
    def tick(self):
        for pawn in self.pawns:
            pawn.tick(self)

        for weapon in self.weapons:
            weapon.tick(self)
        
        for projectile in self.projectiles:
            projectile.tick(self)