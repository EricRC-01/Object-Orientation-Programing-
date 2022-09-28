#Função dada: f(x) = x^3 - x^2 - 13x + 8
def f(x):
    return ( (x*x*x)-(x*x)-(13*x)+8 )

print("Insira o limite inferior e superior:")
a = float(input()) #limite inferior
b = float(input()) #limite superior
c = ((a+b)/2)      #ponto médio

#Considerações iniciais
if( f(a)*f(b) >= 0):
    print("Os valores não tem sínais opostos.")
    print("Logo, não se pode garantir a existência de raízes.")
    quit()

#Looop do calculo da resposta
num_iteracoes = 0
while( f(c) != 0 and f(c) > 0.00000001 and num_iteracoes != 5):
    num_iteracoes = num_iteracoes + 1 
    #Caso: f(c) e f(a) tem sinais opostos -> a raiz está entre a e c
    if (f(c)*f(a) < 0):
        b = c 
    #Consequencia: f(c) e f(b) tem sínais opostos -> a raiz está entre c e b
    else: 
        a = c
    c = ((a+b)/2)

#Saída do programa
print("A raíz é {:.2f}, calculada com {:.2f} iterações"
        .format(f(c),num_iteracoes))