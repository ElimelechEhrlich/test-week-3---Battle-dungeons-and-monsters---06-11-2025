import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc

class Game:
    monsters = [Orc, Goblin]
    def __init__(self):
        pass
    
    def start(self):
        print (self.show_menu())

    def show_menu(self):
        self.choice = input('choice from menu: battle, exit -')
        if self.choice != 'battle' and self.choice != 'exit':
            return self.show_menu()
        elif self.choice == 'exit':
            print ('You are out of the game.')
            return
        return self.choice
    
    def create_player(self, player_name):
        self.player = Player(player_name)

    def choose_random_monster(self, monster_name):
        self.monster = (random.choice(Game.monsters))(monster_name)
        return self.monster.__dict__
    
    def roll_dice(self, sides):
        dice = random.randint(1,sides)
        return dice
    
    def battle(self):
        if self.choice == 'battle':
            player_name = str(input('your name: '))
            monster_name = str(input('monster name: '))
            self.create_player(player_name)
            self.player.set_hp()
            self.player.set_power()
            self.choose_random_monster(monster_name)
            player_roll = self.player.speed + self.roll_dice(6)
            monster_roll = self.monster.speed + self.roll_dice(6)
            if monster_roll > player_roll:
                while self.player.hp > 0 and self.monster.hp > 0:
                    rollspeed = self.roll_dice(20)
                    if self.monster.speed + rollspeed > self.player.armor_rating:
                        print (f'{monster_name}: injury!')
                        rolldamage = self.roll_dice(6)
                        if self.monster.weapon == 'knife':
                            damage = self.player.power + rolldamage*0.5
                        elif self.monster.weapon == 'sword':
                            damage = self.player.power + rolldamage
                        else:
                            damage = self.player.power + rolldamage*1.5
                        self.player.hp -= damage
                    else:
                        print (f'{monster_name}: miss..')
                    rollspeed = self.roll_dice(20)
                    if (self.player.speed + rollspeed) > self.monster.armor_rating:
                        print ('player: injury!')
                        rolldamage = self.roll_dice(6)
                        damage = self.monster.power + rolldamage
                        self.monster.hp -= damage
                    else:
                        print ('player: miss..')
                if self.player.hp <= 0:
                    print ('Death! game over!')
                    return
                elif self.monster.hp <= 0:
                    print ('Well done! you won!')
                    return
            return
    












