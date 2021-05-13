class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        # do attack stuff
        enemy.health -= self.power

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power


gawain = Hero(10, 5)
green_knight = Goblin(6, 2)


def main():

    while green_knight.health > 0 and gawain.health > 0:
        print("You have %d health and %d power." %
              (gawain.health, gawain.power))
        print("The goblin has %d health and %d power." %
              (green_knight.health, green_knight.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            gawain.attack(green_knight)
            print("You do %d damage to the goblin." % gawain.power)
            if green_knight.health <= 0:
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
            gawain.health -= green_knight.power
            print("The goblin does %d damage to you." % green_knight.power)
            if gawain.health <= 0:
                print("You are dead.")


main()
