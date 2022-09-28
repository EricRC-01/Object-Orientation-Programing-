

class Adivinha:
    from random import random

    Maximo = int(input())
    chute = random(Maximo)
    if(chute < 0): chute = chute* (-1)
    verificacao = '='

    while(verificacao != '='):
        if   (verificacao == '>'): chute = chute + 1
        elif (verificacao == '<'): chute = chute - 1

    print(chute)
