# import random
#
# POPULATION = {
#     'monk', 'plumwoman', 'appleman', 'hooker', 'fishwoman', 'butcher',
#     'blacksmith', 'shepherd', 'squire', 'carpenter', 'witchhunter', 'farmer'
# }
# a = random.sample(POPULATION, 3)
#
# print(POPULATION, a, sep='\n')

#ajouter vérification si on passe sur toit ou pas pour savoir si 2 ou 1 point

from math import sqrt


def kingaction(kingpos, knightpos, card, peoplepos):
    actions = dict()
    sqrt(kingpos[0]**2 + kingpos[1]**2)
    kingaction = list()
    kingAP = card[0]
    # on fait avancer le roi d'abord tout droit puis à gauche pour qu'il atteigne le but
    while kingpos[0] != 2 and kingpos[1] != 2 and kingAP > 0:
    # if kingpos != (2, 2):
        if kingpos[1] < 2:
            kingaction.append(('move', kingpos[0], kingpos[1], 'N'))
            #remet la nouvelle position après l'avoir deplace vers le nord
            kingpos = (kingpos[0]-1, kingpos[1])
        elif kingpos[0] > 2:
            kingaction.append(('move', kingpos[0], kingpos[1], 'W'))
            kingpos = (kingpos[0], kingpos[1]-1)

        kingAP -= 1


#on bouge les chevaliers pour qu'ils entourent le roi, on continue tant qu'ils ne sont pas autour
def knightaction(kingpos, knightpos, card, peoplepos):
    knightaction = list()
    knightAP = card[1]
    # while knightAP > 0 and knightpos[1]<10 and knightpos[0]<10:
    # if knightpos == (kingpos[0]-1, kingpos[1]):

        # knightaction.append(('move', knightpos[0], knightpos[1], 'N'))
        # knightpos = (knightpos[0]-1, knightpos[1])
        # knightAP -= 1
    if knightpos != (kingpos[0]-1, kingpos[1]):

        while (knightpos != (kingpos[0]-1, kingpos[1]) and knightAP > 0) and (knightpos != (kingpos[0]+1, kingpos[1]) and knightAP > 0) and (knightpos != (kingpos[0], kingpos[1]+1) and knightAP > 0) and (knightpos != (kingpos[0], kingpos[1]-1) and knightAP > 0):

            if knightpos[1]-kingpos[1] < -1 and knightpos[1]+1<10:
                knightaction.append(('move', knightpos[0], knightpos[1], 'E'))
                knightpos = (knightpos[0], knightpos[1]+1)
                knightAP -= 1

            elif knightpos[1]-kingpos[1] > 1 and knightpos[1]-1>-1:
                knightaction.append(('move', knightpos[0], knightpos[1], 'W'))
                knightpos = (knightpos[0], knightpos[1]-1)
                knightAP -= 1

            elif knightpos[0]-kingpos[0] > 1 and knightpos[0]-1>-1:
                knightaction.append(('move', knightpos[0], knightpos[1], 'N'))
                knightpos = (knightpos[0]-1, knightpos[1])
                knightAP -= 1

            elif knightpos[0]-kingpos[0] < -1 and knightpos[0]+1<10:
                knightaction.append(('move', knightpos[0], knightpos[1], 'S'))
                knightpos = (knightpos[0]+1, knightpos[1])
                knightAP -= 1

    return (knightaction, knightAP)


#on fait avencer le chevalier devant le roi pour laisser la voie libre au roi
def upside_knight(state, kingpos):
    for knightx in range(10):
        for knighty in range(10):
            if state['people'][knightx][knighty] == 'knight':
                if knightx == kingpos[0] - 1 and knighty == kingpos[1]:
                    return 'move', knightx, knighty, 'N'
    return []

def nearest_knight(state, kingpos):
    nearest = (20, 20)
    for knightx in range(10):
        for knighty in range(10):
            if state['people'][knightx][knighty] == 'knight':
                if sqrt(knightx**2 + knighty**2) < sqrt(nearest[0]**2 + nearest[1]**2):
                    nearest = (knightx, knighty)
    return nearest


def kingcoord(state):
    for kingx in range(10):
        for kingy in range(10):
            if state['people'][kingx][kingy] == 'king':
                return (kingx, kingy)

# def farest_knight(state, KNIGHTS):

# def knightscoord(state, KNIGHTS):
#
#                 for i in range(10):
#                     for j in range(10):
#                         if state['people'][i][j] in KNIGHTS: