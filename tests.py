import unittest
from action import *
from combat import *
from magic import *
class CombatSystemTest(unittest.TestCase):
    def setUp(self):
        pass
    def testEntity(self):
        e = Entity()
        self.assertTrue(type(e.stats),dict)
    def testOffensiveSpellCast(self):
        player  = Player(max_hp=50)
        spell   = Fireball(player)
        monster = Entity()
        spell.cast(monster)


if __name__ == "__main__":
    try:
        unittest.main()
    except:
        pass
