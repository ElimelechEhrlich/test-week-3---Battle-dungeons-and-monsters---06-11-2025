import random

class Goblin:
    weapons = ['knife', 'sword', 'axe']
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = 'goblin'
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = random.choice(Goblin.weapons)
    
    def speak(self):
        print (f'I am The terrifying {self.type}!! my name is {self.name}')

    def attack(self):
        return f'{self.type} attack!'
    
    def run_away(self):
            return 'run away!' 

        