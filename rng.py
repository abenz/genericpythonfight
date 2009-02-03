from random import randrange

class Dice:
    @staticmethod
    def roll(dstr='1d6'):
        num_dice,dice_sides=[int(x) 
                             for x in dstr.split('d')]
        return sum([randrange(1,dice_sides+1) 
                    for ex in range(0,num_dice)])

