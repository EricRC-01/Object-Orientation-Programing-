
from ctypes import sizeof
from operator import truth
from pickle import FALSE
from pydoc import apropos
import random
import string


class carta:
    naipe = 0
    valor = 0
    
    def __init__(self, naipe, valor):
        # [ 0 ouros | 1 espada | 2 copas | 3 paus ]
        self.naipe  = naipe
        
        #  [ J = 11 | Q = 12 | K = 13 | A = 14 ]
        self.valor  = valor

    #Função que define o objeto como uma string (toString)
    def __repr__(self):
        return str(self.naipe) + (str(self.valor)) 

class baralho:
    #Atributo: lista de cartas 
    vet_cartas = [] 
    
    #Construtor do baralho
    def __init__(self):
        #Loop para incluir os naipes
        for i in range(4):
            #Loop para incluir os valores 
            for j in range(13):
                nova_carta = carta(i, j+2)
                self.vet_cartas.append(nova_carta)

        random.shuffle(self.vet_cartas)

def ordenar_mao(mao):
    
    vet_valores = []
    vet_naipes = []
    for i in range(len(mao)):
        vet_valores.append(mao[i].valor)
        vet_naipes.append(mao[i].naipe)
    nova_mao = []
    vet_valores.sort()
    vet_naipes.sort()
    
    
    print(vet_valores)
    for i in range(len(mao)):
        encontrou = False
        for j in range(len(vet_valores)):
            for k in range(len(vet_naipes)):
                if(mao[i].valor == vet_valores[j] and mao[i].naipe == vet_naipes[k]):
                    print(carta_em_str(mao[i]))
                    nova_mao.append(mao[i])
                    vet_valores.remove(vet_valores[j])
                    vet_naipes.remove(vet_naipes[k])
                    encontrou = True
                    break
            if(encontrou == True): break
        
        
    
    return nova_mao

#Função para calcular os pontos
def calc_pontos(v_aposta, mao):
    if(len(mao) != 5):
        print("len(mao) != 5 !!!")
        return mao
    
    #Ordenar os valores das cartas das mãoes
    vet_valores = []
    for i in range(len(mao)):
        vet_valores.append(mao[i].valor)
    vet_valores.sort()

    #Verificar se é uma sequenncia
    sequencia = True
    for i in range(len(vet_valores)-1): 
        if( (vet_valores[i]+1) != vet_valores[i+1]): sequencia = False
    if( (vet_valores[3]+1) != vet_valores[4]): sequencia = False

    #Verificar se os naipes são iguais
    naipes_iguais = True
    naipe_comparador = mao[0].naipe 
    for i in range(4):
        if (naipe_comparador != mao[i].naipe): 
            naipes_iguais = False
            
    #Verificar se é uma sequencia real
    sequencia_real = False
    if(sequencia == True and vet_valores[0] == 11): sequencia_real = True
    
    #-----------------Verificar Royal Straight Flush------------- 
    if(sequencia_real == True):
        print("sequencia_real!!")
        return 200*v_aposta
    #-----------------Verificar Straight Flush------------- 
    if(sequencia == True and naipes_iguais == True):
        print("Entrpo: straight flush")
        return 100*v_aposta
    
    #---------------------- Verificar quadra -------------------
    quadra = True
    #Caso: as quatro cartas iguais estão no ínicio
    if(vet_valores[0] == vet_valores[1]): 
        crt_comparadora = vet_valores[0]
        for i in range(0, 4):
            if (crt_comparadora != vet_valores[i]): quadra = False
    #Caso: as quatro cartas iguais estão no final
    else: 
        crt_comparadora = vet_valores[1]
        for i in range(1, 4):
            if (crt_comparadora != vet_valores[i]): quadra = False
    #Verificar e retornar o resultado
    if(quadra == True): 
        print("Quadra !!")
        return 50*v_aposta

    #---------------------- Full hand -------------------
    full_hand = True
    trinca = True
    #Caso: trinca no inicio
    if(vet_valores[0] == vet_valores[2]):
        #Loop para verificar a trinca do inicio
        for i in range(3):
            if(vet_valores[0] != vet_valores[i]): 
                full_hand = False
                trinca = False
        #Verificar se as duas ultimas cartas são iguais
        if(vet_valores[3] != vet_valores[4]): 
            full_hand = False
    #Caso: trinca no final
    else:
        #Loop para verificar a trinca do final
        for i in range(2, 5):
                if(vet_valores[2] != vet_valores[i]): 
                    full_hand = False
                    trinca = False
        #Verificar se as duas primeiras cartas são iguais
        if(vet_valores[0] != vet_valores[1]): 
            full_hand = False
    #Verificar e retornar full hand
    if(full_hand == True): 
        return 20*v_aposta
    #---------------------- Trinca -------------------
    if(trinca == True):
        return 2*v_aposta
    #---------------------- Flush -------------------
        # Obs: a variavel "naipes_iguais" foi declara e definida em 
        # "Royal stright flush" 
    if(naipes_iguais == True): 
        return 10*v_aposta
    #---------------------- Stright -------------------
        # Obs: a variavel "sequencia" foi declara e definida em 
        # "Royal stright flush"
    if(sequencia == True): 
        return 5*v_aposta
    #---------------------- Dois Pares -------------------
    dois_pares = False
    for i in range(4):
        j = 0
        while( j < 4):
            if(mao[i].valor == mao[j].valor): 
                dois_pares = True
            j = j + 1 
    
    if(dois_pares == True): 
        return v_aposta

    return 0    

#Definir a transformar as infos de uma carta (naipe e valor) em string
def carta_em_str(carta):
    #Definir o valor da carta como uma string
    if(carta.valor >= 11):
        if  (carta.valor == 11): valor_str = "J"
        elif(carta.valor == 12): valor_str = "Q"
        elif(carta.valor == 13): valor_str = "K"
        elif(carta.valor == 14): valor_str = "A"
    else: valor_str = str(carta.valor)
    
    #Definir naipe e transforma-lo em string
    naipe_str = ""
    # Caso: ouros
    if(carta.naipe == 0):
        naipe_str = "♦"
    # Caso: espada
    elif(carta.naipe == 1):
        naipe_str = "♠"
    #Caso: copas
    elif(carta.naipe == 2):
        naipe_str = "♥"
    #Caso: paus
    elif(carta.naipe == 3):
        naipe_str = "♣"
    
    carta_str = valor_str + naipe_str
    return carta_str

#Função para transformar uma mão em string 
def mao_em_string(mao):
    string_final = "" 

    #Declarar enquadramento e espaços
    linha_vazia = "|        |"
    enquadramento_superior = "+--------+" 
    enquadramento_inferior = "+--------+" 
    espaco_esq = "|   "
    espaco_dir = "   |"

    #Lista de strings guardando os valores e naipes das cartas 
    infos_cartas = []
    for i in range(len(mao)):
        infos_cartas.append(carta_em_str(mao[i]))
    
    #Definir o enquadramento superior da string (parte acima dos valores)
    for i in range(len(infos_cartas)): 
        string_final += enquadramento_superior + "  "
    string_final += "\n"

    #Definir linha vazia superior 
    for i in range(len(infos_cartas)): 
        string_final += linha_vazia + "  "
    string_final += "\n"

    #Definir meio da string (parte que contem os valores)
    for i in range(len(infos_cartas)):
        string_final += espaco_esq + infos_cartas[i] + espaco_dir
        string_final += "  "
    string_final += "\n"
    
    #Definir linha vazia inferior 
    for i in range(len(infos_cartas)): 
        string_final += linha_vazia + "  "
    string_final += "\n"


    #Definir enquadramento inferior da string (parte abaixo dos valores)
    for i in range(len(infos_cartas)):
        string_final += enquadramento_inferior + "  "
    string_final += "\n"
    
    #Definir identificador das cartas 
    for i in range(len(infos_cartas)):
        string_final += "   ("+ str(i) +")      " 
    
    
    string_final += "\n"
    
    return string_final

#Função para trocar as cartas solicitadas pelo jogador 
def trocar_mao(mao, baralho, inds_cartas):
    nova_mao = []
    for i in range(len(inds_cartas)):
        #Remover uma carta aleatória do baralho
        nova_carta = baralho.vet_cartas.pop()
        #Tirar carta selecionada da mão
        del(mao[int(inds_cartas[i])])
        #Colocar nova carta na mão do jogador
        mao.append(nova_carta)
    return mao


if __name__ == "__main__":


    #Declarações iniciais
    b = baralho()       
    mao_jogador = []    
    creditos_jogador = 200
    banco = 0   

    #Adicionar cartas na mao
    for i in range(5):
        #Pegar uma carta do baralho
        nova_carta = b.vet_cartas.pop()
        #Colocar a carta na mão
        mao_jogador.append(nova_carta)

    #Loop de execução do jogo
    print("||====== Início do jogo ======||")
    comando = ""  
    while(comando != "F"):
        print("\t===> NOVA RODADA <===")
        print("Saldo atual ",creditos_jogador)

        #Leitura do comando
        print("Digite o valor da aposta ou F para terminar")
        comando = input()
        if(comando == "F"): break
        else:
            creditos_jogador -= int(comando) 
            banco += int(comando) 
        #Loop de execução das trocas de cartas
        for i in range(4):
            print("Seu daldo atual: ",creditos_jogador)
            print("Suas cartas são: ")
            print(mao_em_string(mao_jogador))
            print("Digite os números das cartas que deseja trocar ou -1 para finalizar")
            str_aux = input()
            cartas_a_trocar = str_aux.split(" ",6-i)
            if(len(cartas_a_trocar) == 1 and int(cartas_a_trocar[0]) == -1):
                break
            else:
                trocar_mao(mao_jogador,b,cartas_a_trocar)

        #Finalizar rodada
        banco = calc_pontos(banco,mao_jogador)
        print("Parabens, vc ganhou ",banco)
        creditos_jogador += banco
    
    print("Sua pontuação fínal é: ",creditos_jogador)
    print("||====== Fim do jogo ======||")


        
        

    
    
