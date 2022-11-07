from object import *

class WeaponData:
    def __init__(
        self,
        damage_per_shot,
        shots_per_second,
        max_ammo,
        initial_ammo,
        min_ammo
        ):
            self.damage_per_shot = damage_per_shot
            self.shots_per_second = shots_per_second
            self.max_ammo = max_ammo
            self.initial_ammo = initial_ammo
            self.min_ammo = min_ammo

class ProjectileData:
    def __init__(
        self,
        projectile_speed,
        projectile_range
    ):
        self.projectile_speed = projectile_speed
        self.projectile_range = projectile_range


class Weapon(Object):
    def __init__(self, weapon_data, projectile_data):
        super().__init__(self)
        self.weapon_data = weapon_data
        self.projectile_data = projectile_data
        self.ammo = self.weapon_data.initial_ammo

    def tick(self, level):
        super().tick(level)

    def fire(self, heading):
        if self.ammo > self.weapon_data.min_ammo:
            projectile = Projectile(self.projectile_data)
            projectile.heading = heading
            projectile.is_moving = True



class Projectile(Object):
    def __init__(self, projectile_data):
        super().__init__(self)
        self.projectile_data = projectile_data
        self.heading = 0
        self.is_moving = False
    
    def tick(self, level):
        super().tick(level)

