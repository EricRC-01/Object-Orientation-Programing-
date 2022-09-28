import math


#Declaração dos coeficientes
a = 0; b = 0; c = 0 

#Leitura dos coeficientes
print("Insira o valor de a:")
a = float(input())
print("Insira o valor de b:")
b = float(input())
print("Insira o valor de c:")
c = float(input())

#Considerar a = 0
if(a == 0):
    print("Não é possível dividr por 0\n (a = 0)")
    exit()

#Considerar delta < 0 
delta = (b*b) - (4*a*c)
if(delta < 0):
    print("Delta = 0, logo não existem raizes reais")
    exit()

#Calculo das raízes x1 e x2
x1 = ( (-b) + math.sqrt(delta) ) / (2*a)
x2 = ( (-b) - math.sqrt(delta) ) / (2*a)

#Saida 
print("X1 = {:.2f} X2 = {:.2f}".format(x1,x2))
