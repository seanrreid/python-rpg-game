from character import Character
import random
import time

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 0
        self.power = 4
        self.coins = 4
    def alive(self):
        return True
    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        #if self.health <= 0:
        #    print("{} is dead.".format(self.name))