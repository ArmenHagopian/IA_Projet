# import random
#
# POPULATION = {
#     'monk', 'plumwoman', 'appleman', 'hooker', 'fishwoman', 'butcher',
#     'blacksmith', 'shepherd', 'squire', 'carpenter', 'witchhunter', 'farmer'
# }
# a = random.sample(POPULATION, 3)
#
# print(POPULATION, a, sep='\n')
from math import sqrt
def position(kingpos, knightpos, card, peoplepos):
    actions = dict()
    sqrt(kingpos[0]**2 + kingpos[1]**2)
    kingaction = list()
    knightaction = list()
    kingAP = card[0]
    knightAP = card[1]
    # on fait avancer le roi d'abord tout droit puis à gauche pour qu'il atteigne le but
    while kingpos[0] != 2 and kingpos[1] != 2 and kingAP > 0:
    # if kingpos != (2, 2):
        if kingpos[1] < 2:
            kingaction += ('move', kingpos[0], kingpos[1], 'N')
            #remet la nouvelle position après l'avoir deplace vers le nord
            kingpos = (kingpos[0]-1, kingpos[1])
        elif kingpos[0] > 2:
            kingaction += ('move', kingpos[0], kingpos[1], 'W')
            kingpos = (kingpos[0], kingpos[1]-1)

        kingAP -= 1
#on bouge les chevaliers pour qu'ils entourent le roi, on continue tant qu'ils ne sont pas autour
    while (knightpos != (kingpos[0]-1, kingpos[1]) and knightAP > 0) or (knightpos != (kingpos[0]+1, kingpos[1]) and knightAP > 0) or (knightpos != (kingpos[0], kingpos[1]+1) and knightAP > 0) or (knightpos != (kingpos[0], kingpos[1]-1) and knightAP > 0):
        if knightpos[0]-kingpos[0] > 0:
            knightaction += ('move', knightpos[0], knightpos[1], 'E')
            knightpos = (knightpos[0], knightpos[1]+1)

        kingAP -= 1

