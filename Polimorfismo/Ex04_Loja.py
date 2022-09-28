
# Loja


class produto:
    codigo_de_barras = 0
    nome = ""
    quantidade_estoque = 0
    
class livros(produto):
    qnt_paginas = 0
    nome_autor = 0

class DVD(produto):
    nome_diretor = ""
    categoria = ""

class CD(produto):
    nome_musico = ""
    tempo_duracao_h = 0


class Loja(produto):
    lista_CDs = []
    lista_Livros = []
    lista_DVDs = []

    def encontrar_livro(self, codigo):
        for i in len(range(self.lista_Livros)):
            if(codigo == self.lista_Livros[i].codigo_de_barras):
                return self.lista_Livros[i]
        print("Este item não foi encontrado em estoque")
     
    def encontrar_CDs(self, codigo):
        for i in len(range(self.lista_CDs)):
            if(codigo == self.lista_CDs[i].codigo_de_barras):
                return self.lista_CDs[i]
        print("Este item não foi encontrado em estoque")
    
    def encontrar_DVDs(self, codigo):
        for i in len(range(self.lista_DVDs)):
            if(codigo == self.lista_DVDs[i].codigo_de_barras):
                return self.lista_DVDs[i]
        print("Este item não foi encontrado em estoque")

    def qnt_estoque(self):
        return(len(self.lista_CDs) + len(self.lista_DVDs) + len(self.lista_Livros))
