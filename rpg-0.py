# Hero class.
class Character():

    def __init__(self, name, health, power):
        self.power = power
        self.health = health
        self.name = ""
    
    def isAlive(self):
        if (self.health <= 0):
            return False
        else: return True
    def attack(self, defender):
        if isinstance(defender, zombie):
            print('you are here.')
            pass
        else:
            defender.health = defender.health - self.power
            return defender.health

    def printHealth(self):
        print("The health of the {} is {} and the power is {}".format(self.name, self.health, self.power))
    
    def choice(self, other ):
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The {} has {} health and {} power.".format(other.name, other.health, other.power))
        print()
        print("What do you want to do?")
        print("1. fight {}".format(other.name))
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            self.attack(other)
            print("You do {} damage to the {}.".format(self.power , other.name ))
            if other.health <= 0:
                print("The {} is dead.".format(other.name))
        elif user_input == "2":
            return 2
        elif user_input == "3":
            print("Goodbye.")
            return 3
        else:
            print("Invalid input %r" % user_input)




class hero(Character):
    health = 10
    power = 4
    name = ""

    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name

class zombie(Character):
    power = 2

    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

# goblin class
class goblin(Character):
    health = 6
    power = 2
    name = ""
    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name


def game(hero, enemy):
    while (hero.isAlive() and enemy.isAlive()):
        hero.choice(enemy)
        print("you made it past choice.")
        enemy.attack(hero)



        
zard = zombie("zardilla",1,2)    
goblin = goblin("goblin",6, 2)
hero = hero("hero", 10, 5)
game(hero, zard)
