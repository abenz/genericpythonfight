from rng import Dice

class SpellEffect:
    spell = None
    def __init__(self,stat,strength,**kwargs):
        self.stat = stat
        self.strength = strength
        self.duration = kwargs.get('duration',0)
    def affect(self,target):
        pass

class Damage(SpellEffect):
    def affect(self,target):
        target.stats[self.stat] -= Dice.roll(self.strength)
        
class Ameliorate(SpellEffect):
    def affect(self,stat,strength,target):
        target.stats[self.stat] += Dice.roll(self.strength)

class Element:
    strong_against = []
    weak_against = []
class WaterElement(Element):
    strong_against = ['Earth']
    weak_against = ['Fire']
class FireElement(Element):
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
    def __init__(self, caster, **kwargs):
        self.caster = caster
        self.level = kwargs.get('level',1)
    def cast(self,target):
        for effect in self.effects:
            effect.affect(target)

class Fireball(Spell):
    def __init__(self,caster,**kwargs):
        Spell.__init__(self, caster, **kwargs)
        self.name = "Fireball Level %s" % self.level
        self.element = FireElement()
        self.strength = "%sd%s" % (self.level,6)
        self.effects = [
            Damage('hp',self.strength)
            ]

class Heal(Spell):
    stats_affected = ['hp']
    def __init__(self,**kwargs):
        self.name = "Heal Level %s" % self.level
        self.strength = "%sd%s" % (self.level,4)
        self.effects = [
            Ameliorate('hp',self.strength)
            ]
        Spell.__init__(self, caster, **kwargs)

class SpellBook:
    spells = []
