

print("Insira o valor a ser calculado")
X = float(input())

print("Insira o chute inicial")
chute_inicial = float(input())

raiz_atual = chute_inicial
raiz_anterior = 0
while( (raiz_atual - raiz_anterior) > 0.00000001):
    raiz_anterior = raiz_atual
    raiz_atual = (raiz_anterior + (X/raiz_anterior)) / 2
    #Pint test
        #print("raiz_atual = {:.3f} raiz_anterior = {:.3f}".format( raiz_atual, raiz_anterior) )

    

print("O valor da raiz de {:.2f} é {:.2f}".format(X,raiz_atual))


