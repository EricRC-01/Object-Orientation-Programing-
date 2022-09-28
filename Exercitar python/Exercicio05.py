


def verPrimo(numero):
    
    for i in range(2,numero):
        if(numero % i == 0):
            return False
    return True

def main():

    print("Insira um número inteiro")
    numero = int(input())

    i = numero - 1
    while(i > 1):
        if(verPrimo(i)):
            print("O menor número primo é ",i)
            quit()

        i -= 1
    print("Não existe numero primo menor que ",numero)  
    

if __name__ == "__main__":
    main()

