def modulo(x):
    if(x < 0): return (-(x))
    else: return x

#Função dada
#f(x) = x^3 - x^2 - 13x + 8
def f(x):
    return ( (x*x*x) - (x*x) -(13*x) + 8 )

#Derivada da função dada:
#f'(x) = 3x^2 - 2x  - 13
def f_linha(x):
    return ( (3*x*x) - (2*x) - 13 )

#Input inicial
print("Insira o valor do chute inicial")
chute_inicial = float(input())
raiz_anterior = chute_inicial

#Calculo inicial
raiz_atual = raiz_anterior - ( f(raiz_anterior)/f_linha(raiz_anterior))
raiz_anterior = raiz_atual

#Loop de resolução
while(modulo(raiz_atual - raiz_anterior) > 0.00000001):
    raiz_atual = raiz_anterior - ( f(raiz_anterior)/f_linha(raiz_anterior))
    raiz_anterior = raiz_atual

#Saída do programa
print("O valor da raíz é",raiz_atual)
