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

    def printHealth(self):
        print("The health of the {} is {} and the power is {}".format(self.name, self.health, self.power))
    
    def choice(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            attack(hero, goblin)
            print("You do {} damage to the goblin.".format(self.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            return 2
        elif user_input == "3":
            print("Goodbye.")
            return 3
        else:
            print("Invalid input %r" % user_input)

def attack(attacker, defender):
    defender.health = defender.health - attacker.power
    return defender.health


class hero(Character):
    health = 10
    power = 4
    name = ""

    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name

# goblin class
class goblin(Character):
    health = 6
    power = 2
    name = ""
    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name


def game():
    while (hero.isAlive() and goblin.isAlive()):
        hero.choice()
       
        attack(goblin,hero)

        
    
goblin = goblin("goblin",6, 2)
hero = hero("hero", 10, 5)
game()
