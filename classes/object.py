from level import *

class Object:
    def __init__(self):
        self.position = [0, 0]
        self.heading = 0
        self.add_to_level_queue = []
    
    def tick(self, level):
        for object in self.add_to_level_queue:
            level.objects.append(object)

        self.add_to_level_queue.clear()

    def turn(self, heading):
        self.heading = heading
    
    def attack(self, heading):
        self.turn(heading)
        self.weapon.fire(heading)