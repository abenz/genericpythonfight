from action import *

class Entity:
    def __init__(self, *args, **kwargs):
        self.stats = {'hp'               : kwargs.get('hp',1),
                      'max_hp'           : kwargs.get('max_hp',1),
                      'mp'               : kwargs.get('mp',0),
                      'max_mp'           : kwargs.get('max_mp',0),
                      'level'            : kwargs.get('level',0),
                      'initiative'       : kwargs.get('initiative',0),
                      'possible_actions' : kwargs.get('possible_actions',[]),
                      'location'         : kwargs.get('location',(0,0,0)),}

class Combatant(Entity):
    def __init__(self,**kwargs):
        Entity.__init__(self,**kwargs)
    def act(self):
        pass

class Monster(Combatant):
    def __init__(self,**kwargs):
        Entity.__init__(self,**kwargs)
    def act(self):
        action = self.possible_actions[randrange(0,len(possible_actions))]
        action.execute()
        
class Player(Combatant):
    def act(self):
        pass

class BattleGround:
    size=(0,0,0)
    def __init__(self,**kwargs):
        pass
    def draw(self):
        pass

