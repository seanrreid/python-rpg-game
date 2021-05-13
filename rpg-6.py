import random

class Character:
    def __init__(self, name, health=10, power=5):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))


class Hero(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return True

gawain = Hero("Sir Gawain", 20, 8)
green_knight = Goblin("The Green Knight", 20, 5)
zombie = Zombie("Undead", 0, 2)

enemies = [zombie, green_knight]

def main():

    while green_knight.alive() > 0 and gawain.alive() > 0:
        gawain.print_status()
        green_knight.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ")
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            gawain.attack(green_knight)
            print("You do %d damage to the goblin." % gawain.power)
            if green_knight.alive() == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if green_knight.health > 0:
            random_index = random.randrange(len(enemies))
            enemy = enemies[random_index]
            enemy.attack(gawain)
            print("The %s does %d damage to you." % (enemy.name, enemy.power))
            if gawain.alive() == False:
                print("You are dead.")


main()
