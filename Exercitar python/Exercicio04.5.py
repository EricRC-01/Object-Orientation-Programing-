

print("Insira um número inteiro")
numero = int(input())

for i in range(2,numero):
    if(numero % i == 0):
        print("O número {} não é primo, seu menor divisor é {}".format(numero,i))
        quit()

print("O número {} é primo".format(numero))
