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
        if self.speed + rollspeed > player.armor_rating:
            print (f'{self.name}: injury!')
            rolldamage = self.roll_dice(6)
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
    
