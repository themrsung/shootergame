import math
from object import *
from weapon import *

class PawnData:
    def __init__(self, max_health, initial_health, death_health, min_health, default_weapon):
        self.max_health = max_health
        self.initial_health = initial_health
        self.death_health = death_health
        self.min_health = min_health
        self.default_weapon = default_weapon

class Pawn(Object):
    def __init__(self, pawn_data):
        super().__init__(self)
        self.pawn_data = pawn_data
        self.heatlh = self.pawn_data.initial_health
        self.is_dead = False
        self.weapon = self.pawn_data.default_weapon
    
    def tick(self, level):
        super().tick(level)
        if self.heatlh <= self.death_health:
            self.die()
    
    def die(self):
        self.is_dead = True
    
    def take_damage(self, amount):
        self.health = math.max(self.health - amount, self.pawn_data.min_health)

    def heal(self, amount):
        self.health = math.min(self.health + amount, self.pawn_data.max_health)
    
    