"""

Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time
import character
from hero import Hero
from medic import Medic
from shadow import Shadow
from zombie import Zombie
from goblin import Goblin
from wizard import Wizard


class Battle():

    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
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
            print("YOU LOSE!")
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