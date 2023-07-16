"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import colorama
import random

color = colorama.Fore

class Entity:
    def __init__(self, name:str, health:int, power:int):
        self.name = name
        self.health = health
        self.power = power
        self.alive = self.health > 0

    def take_damage(self, other):
        """
        take damage from another Entity and update alive flag

        Args:
            other (Entity): the attacking Entity from which this will get damaged
        """
        self.health -= other.power
        if self.health <= 0:
            print(f"{color.MAGENTA}{self.name} {color.RED}got hit by {color.MAGENTA}{other.name} {color.RED}with a deadly attack{color.RESET}")
            self.alive = False
        else:
            print(f"{color.MAGENTA}{self.name} {color.YELLOW}got attacked by {color.MAGENTA}{other.name} {color.YELLOW}losing {color.RED}{other.power} {color.YELLOW}hp{color.RESET}")

    def attack(self, other):
        """
        attack other Entity by using the `take_damage`method

        Args:
            other (Entity): the other entity to deal damage on
        """
        if not self.alive:
            return # cant attack if Entity is dead
        other.take_damage(self)

    def do_nothing(self, other):
        """
        Show if Entity missed a chance on other by doing nothing

        Args:
            other (Entity): the other that this Entity could have attacked
        """
        if other.health-self.power <= 0: # missed a chance
            print(f"{color.MAGENTA}{self.name} {color.RED} missed his chance to kill {color.MAGENTA}{other.name}{color.RESET}")
        else:
            print(f"{color.MAGENTA}{self.name} {color.YELLOW}did nothing on this round{color.RESET}")

    def flee(self, other):
        """
        By running away the other entity wins automatically

        Args:
            other (Entity): other entity that will win after this action
        """
        print(f"{color.MAGENTA}{self.name} {color.RED}flee. {color.MAGENTA}{other.name} {color.GREEN}won!!{color.RESET}")
        self.alive = False

    def make_decision(self, other, rounds_played:int):
        """
        Let this Entity choose his next action based on the amount off
        rounds played and the other Entity

        Args:
            other (Entity): the entity this entity is fighting against
            rounds_played (int): how many rounds are played already
        """
        self.attack(other) # for now just attack, but here could be a algorithm to play intelligent against the other

    def show_stat(self):
        print(f"{color.MAGENTA}{self.name} {color.GREEN}has {color.YELLOW}{self.health} {color.GREEN}health and {color.YELLOW}{self.power} {color.GREEN}power.{color.RESET}")

def ask_for_action(hero:Entity, goblin:Entity) -> str:
    """
    Show the stats of the hero and goblin and ask for a
    action. no validation of input

    Returns:
        str: user action
    """
    hero.show_stat()
    goblin.show_stat()
    print()
    print(f"{color.CYAN}What do you want to do?{color.RESET}")
    print(f"{color.RED}1. fight goblin{color.RESET}")
    print(f"{color.YELLOW}2. do nothing{color.RESET}")
    print(f"{color.LIGHTBLUE_EX}3. flee{color.RESET}")
    user_input = input(color.MAGENTA+"> "+color.CYAN)
    print(color.RESET, end="\r")
    return user_input

def main():
    rounds_played = 0
    hero = Entity("Hero", 10, 5)
    goblin = Entity("Goblin", random.randint(2, 13), random.randint(1, 3))

    while goblin.alive and hero.alive:
        user_input = ask_for_action(hero, goblin)
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            hero.do_nothing(goblin)
        elif user_input == "3":
            hero.flee(goblin)
            break
        else:
            print("Invalid input %r" % user_input)

        goblin.make_decision(hero, rounds_played)

        rounds_played += 1

if __name__ == "__main__":
    main()
