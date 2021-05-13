class Character:
    def __init__(self, name, health=10, power=5):
        self.health = health
        self.power = power

    def attack(self, enemy):
        # do attack stuff
        enemy.health -= self.power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

gawain = Hero("Sir Gawain", 20, 10)
green_knight = Goblin("The Green Knight", 6, 2)

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
            # Goblin attacks hero
            green_knight.attack(gawain)
            print("The goblin does %d damage to you." % green_knight.power)
            if gawain.alive() == False:
                print("You are dead.")


main()
