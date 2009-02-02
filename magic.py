from rpg import Dice

class SpellEffect:
    spell = None
    def __init__(self,spell,**kwargs):
        self.spell = spell
        self.stats_affected = kwargs.get('stats_affected',[])
        self.duration = kwargs.get('duration',0)
    def affect(self,target):
        for stat in self.stats_affected:
            d = Dice(
            target['stat'] = target['stat'] - self.spell.
class Damage(SpellEffect):
    pass
        
class Ameliorate(SpellEffect):
    pass

class Element:
    strong_against = []
    weak_against = []
class Water(Element):
    strong_against = ['Earth']
    weak_against = ['Fire']
class Fire(Element):
    strong_against = ['Water','Dark']
    weak_against = ['Earth']

class Spell:
    stats_affected = {}
    area_of_effect = 1
    level = 1
    strength = '1d1'
    element = Element() 
    name = "unset"
    valid_targets = []
    duration = 1
    status_affected = []
    def cast(self,target):
        for effect in self.effects:
            effect.affect(target)

class Fireball(Spell):
    def __init__(self,**kwargs):
        self.caster = None
        self.level = kwargs.get('level',1)
        self.name = "Fireball Level %s" % self.level
        self.element = Fire()
        self.strength = "%sd%s" % (self.level,4)
        self.effects = [
            Damage(self,stats_affected={'hp':
                                            {'amount':self.strength}
                                        })
            ]
class Heal(Spell):
    stats_affected = ['hp']
    def __init__(self,**kwargs):
        self.caster = None        
        self.level = kwargs.get('level',1)
        self.name = "Heal Level %s" % self.level
        self.strength = "%sd%s" % (self.level,4)
        self.effects = [
            Ameliorate(self,'hp')
            ]

class SpellBook:
    spells = []
    
if __name__ == '__main__':
    f=Fireball(level=3)
    print f.strength


    
