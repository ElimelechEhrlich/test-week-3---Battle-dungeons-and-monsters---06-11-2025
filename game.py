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
        return self.player

    def choose_random_monster(self, monster_name):
        self.monster = (random.choice(Game.monsters))(monster_name)
        return self.monster
    
    def roll_dice(self, sides):
        dice = random.randint(1,sides)
        return dice
    
    def play_game(self):
        if self.choice == 'battle':
            player_name = str(input('your name: '))
            monster_name = str(input('monster name: '))
            self.player = self.create_player(player_name)
            self.player.set_hp()
            self.player.set_power()
            self.monster = self.choose_random_monster(monster_name)
            player_roll = self.player.speed + self.roll_dice(6)
            monster_roll = self.monster.speed + self.roll_dice(6)
            if monster_roll > player_roll:
                return self.battle(self.monster, self.player)
            else:
                return self.battle(self.player, self.monster)
    
    def battle(self, current_player, rival ):
        while current_player.hp > 0 and rival.hp > 0:
            damage = 0
            rollspeed = self.roll_dice(20)
            current_player.attack()
            return self.battle(rival, current_player)
        if self.player.hp <= 0:
            print ('Death! game over!')
            return
        elif self.monster.hp <= 0:
            print ('Well done! you won!')
            return


    












