from actions import *

class Entity:
    hp=1;max_hp=1
    mp=0;max_mp=0
    level=0
    possible_actions=[]

class Combatant(Entity):
    def __init__(self,**kwargs):
        self.possible_actions = [WaitAction(self)]
        self.max_hp = kwargs.get('max_hp',1)
        self.combatant_type = kwargs.get('combatant_type')
        self.level = kwargs.get('level',1)
    def act(self):
        pass

class Monster(Combatant):
    def act(self):
        action = self.possible_actions[randrange(0,len(possible_actions))]
        action.execute()
        
class Player(Combatant):
    def act(self):
        pass

class BattleGround:
    def __init__(self,**kwargs):
        pass
        
    def draw(self):
        pass

