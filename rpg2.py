"""

Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time


class Character():
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 0


    def alive(self):
        return self.health > 0


    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(0.5)

    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    inventory = []
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 8
        self.armor = 0
        self.evade = 0

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
            print("$$$$$$$$$$$$$$$$$$$")
            print("{} got a bounty of {}".format(self.name, enemy.coins))

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

class Shadow(Character):
    def __init__(self):
            self.name = 'Shadow'
            self.health = 1
            self.power = 6
            self.coins = 10

    def receive_damage(self, points):
        chance = random.randint(1,10)
        if chance == 1:
            self.health -= points
        else:
            print("{} evades your attack.".format(self.name))
            pass
        if self.health <= 0:
            print("{} is dead.".format(self.name))

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


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 4
    
# !!!!!!!!!!   def bounty (self):

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle():

    def do_battle(self, hero, enemy):
        print("=======")
        print("Hero faces the {}".format(enemy.name))
        print("=======")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.0)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
                enemy.attack(hero)
            elif keyinput == 2:
                enemy.attack(hero)
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                enemy.attack(hero)
                continue
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            hero.bounty(enemy)
            return True
        else:
            #print("YOU LOSE!")
            return False


class Tonic():
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class SuperTonic():
    cost = 7
    name = 'Super Tonic'
    def apply(self, character):
        character.health = 10
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword():
    #def __init__(self, cost, name):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Armor():
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print("{}'s armor increased to {}.".format(hero.name, hero.armor))

class Evade():
    cost = 10
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print("{}'s evade increased to {}.".format(hero.name, hero.evade))



class Store():
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]

    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            input1 = int(input("> "))
            if input1 == 10:
                break
            else:
                if hero.coins >= item.cost:
                    ItemToBuy = Store.items[input1 - 1]
                    item = ItemToBuy()
                    hero.buy(item)
                else:
                    print("You don't have enough coins for that.")


if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard(), Shadow()]
    battle_engine = Battle()

    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)
    print("YOU WIN!")