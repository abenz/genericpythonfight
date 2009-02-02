from random import randrange

class Dice:
    def __init__(self,dstr='1d6'):
        self.num_dice,self.dice_sides=[int(x) 
                                       for x in dstr.split('d')]
    def roll(self):
        return sum([randrange(1,self.dice_sides+1) 
                    for ex in range(0,self.num_dice)])

class Profession:
    actions = []


if __name__ == '__main__':
    d = Dice('1d20')
    for i in range(0,200):
        d.roll()
