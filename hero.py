import time
import random
from character import Character

class Hero(Character):
    inventory = []
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 2

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1.0)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        power_multip = 1
        chance = random.randint(1,5)
        if chance == 1:
            power_multip = 2
            print("**** {} got a critical hit****".format(self.name))
        else:
            power_multip = 1
        enemy.receive_damage(self.power * power_multip)

    def bounty(self, enemy):
        if enemy.health <= 0:
            self.coins += enemy.coins
            print("$$$ {} got a bounty of {}".format(self.name, enemy.coins))

    def receive_damage(self, points):
        evasion_chance = 10
        chance = random.randint(1, evasion_chance)
        if self.evade > 0 and self.evade < 10:
            if chance == 1:
                print("{} evades {}".format(self.name, enemy.name))
                return
        elif self.evade >= 2:
            evasion_mult = 0
            while evasion_mult < self.evade:
                evasion_chance = 10 - 0.5 * evasion_mult
                evasion_mult += 2
                return evasion_chance
            print("{} evades {}".format(self.name, enemy.name))
        else:
            self.health -= points + self.armor 
