from character import Character
import time
import random

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 0
        self.coins = 2
    def receive_damage(self, points):
        chance = random.randint(1,5)
        if self.receive_damage(points):
            if chance == 1:
                self.health -= points
                self.health += 2
            else:
                self.health -= points
        if self.health <= 0:
            print("{} is dead.".format(self.name))