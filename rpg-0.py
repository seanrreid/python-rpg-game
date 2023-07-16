"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
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
            print(f"{self.name} got hit by {other.name} with a deadly attack")
            self.alive = False
            return
        print(f"{self.name} got attacked by {other.name} losing {other.power} hp")

    def attack(self, other):
        """
        attack other Entity by using the `take_damage`method

        Args:
            other (Entity): the other entity to deal damage on
        """
        other.take_damage(self)

    @property
    def stats(self) -> tuple:
        return self.health, self.power

def ask_for_action(hero:Entity, goblin:Entity) -> str:
    """
    Show the stats of the hero and goblin and ask for a
    action. no validation of input

    Returns:
        str: user action
    """
    print("You have %d health and %d power." % hero.stats)
    print("The goblin has %d health and %d power." % goblin.stats)
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    return input("> ")

def main():
    hero = Entity("Hero", 10, 5)
    goblin = Entity("Goblin", 6, 2)

    while goblin.alive and hero.alive:
        user_input = ask_for_action(hero, goblin)
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive:
            goblin.attack(hero)

if __name__ == "__main__":
    main()
