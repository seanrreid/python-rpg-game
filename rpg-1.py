import random

class Hero(Character):
    # hero_health = 0
    # hero_power = 0

    def __init__(self):
        self.health = random.randint(10, 15)
        self.power = round(self.health/2)
        # hero_health = self.health
        # hero_power = self.power

    def hero_attack(self, goblin):
        goblin.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def display_menu(self):
        print("You have {} health and {} power.".format(rus.health, rus.power))
        print("The goblin has {} health and {} power.".format(gus.health, gus.power))

        print("Choose your option: ")
        print("1 -- Fight the goblin")
        print("2 -- Run from the goblin")
        print("3 -- Do nothing")

    def choose_action(self,opp):
        while gus.alive() == True and rus.alive() == True:
            rus.display_menu()
            user_input = input()
            if user_input == "1":
                rus.hero_attack(gus)
                gus.goblin_attack(rus)
                if gus.health <= 0:
                    print("You have slayed the beast!")
                if rus.health <= 0:
                    print("You have been slain. =(")
            elif user_input == "2":
                print("You ran like a coward.")
                gus.goblin_attack(rus)
                if rus.health <= 0:
                    print("You have been slain. =(")
                break
            elif user_input == "3":
                gus.goblin_attack(rus)
                gus.goblin_attack(rus)
                gus.goblin_attack(rus)
                if rus.health <= 0:
                    print("You have been slain. =(")
                
            else:
                print("Invalid input. Try again")

class Goblin(Character):

    # goblin_health = 
    # goblin_power = 

    def __init__(self):
        self.health = random.randint(5, 10)
        self.power = round(self.health/3)

    def goblin_attack(self, hero):
        hero.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

gus = Goblin()
mike = Goblin()
rus = Hero()
# rus.display_menu()
rus.choose_action()


class Character:

