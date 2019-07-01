"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character():
    def __init__(self,health,power,name):
        self.health = health
        self.power = power
        self.name = name
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, other):
        other.health -= self.power
        print("The %s does %d damage to the %s." %( self.name ,self.power, other.name))
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name,self.health, self.power))

class Hero(Character):
    def __init__(self,health, power, name):
        super().__init__(health, power, name)
    # def attack(self, other):
    #     other.health -= self.power
    #     print("You do %d damage to the goblin." % self.power)
    #     if other.health <= 0:
    #             print("The goblin is dead.")
    # def print_status(self):
    #     print("You have %d health and %d power." % (self.health, self.power))



class Goblin(Character):
    def __init__(self,health, power, name):
        super().__init__(health, power, name)
    # def attack(self, other):
    #     other.health -= self.power
    #     print("The goblin does %d damage to you." % self.power)
    # def print_status(self):
    #     print("The goblin has %d health and %d power." % (self.health, self.power))

class Zombie(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)


def main():
    hero = Hero(10, 5, "hero")
    goblin = Goblin(6,2, "goblin")
    zombie = Zombie(1000, 3, "zombie")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            #Hero attacks goblin or zombie
            hero.attack(goblin)
            #hero.attack(zombie)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
