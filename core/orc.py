import random
class Orc:
    weapons = ['knife', 'sword', 'axe']
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = 'orc'
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = random.choice(Orc.weapons)
    
    def speak(self):
        print (f'I am The terrifying {self.type}!! my name is {self.name}')

    def attack(self):
        return f'{self.type} attack!'
    