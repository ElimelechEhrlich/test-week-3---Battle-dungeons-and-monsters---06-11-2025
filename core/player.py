import random

class Player:
    professions = ['fighter', 'healer']
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = random.choice(Player.professions)

    def set_hp(self):
        if self.profession == 'healer':
            self.hp += 10
        
    def set_power(self):
        if self.profession == 'fighter':
            self.power += 2
    
    def speak(self):
        print (f'my name is {self.name}, and my profession is {self.profession}')

    def attack(self):
        return f'{self.profession} attack'
