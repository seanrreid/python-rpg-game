from character import Character
import random
import time

class Shadow(Character):
    def __init__(self):
            self.name = 'Shadow'
            self.health = 1
            self.power = 1
            self.coins = 3

    def receive_damage(self, points):
        chance = random.randint(1,10)
        if chance == 1:
            self.health -= points
        else:
            print("{} evades your attack.".format(self.name))
            pass
        if self.health <= 0:
            print("{} is dead.".format(self.name))