class Object:
    def __init__(self):
        self.position = [0, 0]
        self.heading = 0
    
    def tick(self):
        pass

    def turn(self, heading):
        self.heading = heading
    
    def attack(self, heading):
        self.turn(heading)
        self.weapon.fire(heading)