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
        if self.speed + rollspeed > player.armor_rating:
            print (f'{self.name}: injury!')
            rolldamage = roll_dice(6)
            if self.weapon == 'knife':
                damage = self.power + rolldamage*0.5
            elif self.weapon == 'axe':
                damage = self.power + rolldamage*1.5
            elif self.weapon == 'sword':
                damage = self.power + rolldamage
            player.hp -= damage
        else:
            print (f'{self.name}: miss..')
            return
    
    def run_away(self):
            return 'run away!' 

        
