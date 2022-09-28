# /************************************************************
# *            Eric Rodrigues das Chagas                      *
# *    [ICMC - Bacharelado em Ciências da Computação - 2021]  *
# *    NºUSP: 12623971                                        *
# * ||----------------------Contatos----------------------||  *
# *            Telegram [ @EricRC_123 ]                       *
# *            Email  [ eric.r.c@usp.br ]                     *
# *************************************************************/




class Pessoa:
    nome = str 
    email = str
    endereço = str
    inscri_estadual = str
    
    def pessoa_to_str(self):
        str_final = ""
        str_final += "Nome:" + self.nome + "\n"
        str_final += "email: " + self.email + "\n"
        str_final += "Inscrição estadual: " + self.inscri_estadual + "\n" 
        return str_final

class CPF(Pessoa):
    num_CPF = 0
    data_nascimento = str
    estado_civil = str

    def __str__(self):
        str_final = "\t<------ Novo individuo ------>\n"
        str_final += self.pessoa_to_str()
        str_final += "CPF: " + str(self.num_CPF) + "\n"
        str_final += "Data de nascimento: " + self.data_nascimento + "\n"
        str_final += "Estado civil: " + self.estado_civil + "\n"
        str_final += "\t<---------------------------->\n"
        str_final += "\n"
        return str_final

class CNPJ(Pessoa):
    num_CNPJ = 0
    razão_social = str
    data_de_abertura = str

    def __str__(self):
        str_final = "\t<------ Novo individuo ------>\n"
        str_final += self.pessoa_to_str()
        str_final += "CNPJ: " + str(self.num_CNPJ) + "\n"
        str_final += "Data de abertura " + self.data_de_abertura + "\n"
        str_final += "Razão social: " + self.razão_social + "\n" 
        str_final += "\t<---------------------------->\n"
        str_final += "\n"
        return str_final
        
class Agenda():
    CPFs_list = []
    CNPJs_list = []

    def encontrar_CPF(self, cpf_buscado):
        for i in len(range(self.CPFs_list)):
            if(cpf_buscado == self.CPFs_list[i].num_CPF):
                return self.CPFs_list[i]
            else:
                print("ERROR: encontrar_CPF > Número CPF não encontrado")
                return -1

    def encontrar_CNPJ(self, cnpj_buscado):
        for i in len(range(self.CNPJs_list)):
            if(cnpj_buscado == self.CNPJs_list[i].num_CNPJ):
                return self.CNPJs_list[i]
            else:
                print("ERROR: encontrar_CNPJ > Número CNPJ não encontrado")
                return -1

    def remover_CPF(self, num_CPF):
        self.CPFs_list.remove(self.encontrar_CPF(num_CPF))

    def remover_CNPJ(self, num_CNPJ):
        self.CNPJs_list.remove(self.encontrar_CNPJ(num_CNPJ))

    def add_CPFs(self, qnt_cpfs):
        for i in qnt_cpfs:
            novo_CPF = CPF
            novo_CPF.nome = input()
            novo_CPF.email = input()
            novo_CPF.endereço = input()
            novo_CPF.inscri_estadual = input() 
            novo_CPF.num_CPF = input() 
            novo_CPF.data_nascimento = input() 
            novo_CPF.estado_civil = input()
            self.CPFs_list.append(novo_CPF)
    
    def add_CNPJs(self, qnt_cnpjs):
        for i in qnt_cnpjs:
            novo_CNPJ = CNPJ
            novo_CNPJ.nome = input()
            novo_CNPJ.email = input()
            novo_CNPJ.endereço = input()
            novo_CNPJ.inscri_estadual = input() 
            novo_CNPJ.num_CNPJ = input() 
            novo_CNPJ.data_de_abertura = input() 
            novo_CNPJ.razão_social = input()
            self.CNPJs_list.append(novo_CNPJ)

    def ordenar_CPFs(self):
        #Passar lista os números dos CPFs para uma lista auxiliar
        list_Aux = []
        for i in len(self.CPFs_list):
            list_Aux.append(self.CNPJs_list[i].num_CPF)
        
        #Ordenar lista auxiliar
        list_Aux.sort()

        #Passar lista dos CPFs a partir da lista auxiliar 
        CPFs_ordenados = []
        for i in len(range(self.CPFs_list)):
            #Encontrar primeiro CPF
            novo_CPF = CPF
            novo_CPF = self.encontrar_CPF(list_Aux[i])
            
            #Passar novo CPF para a lista de CPFS ordenados            
            CPFs_ordenados.append(novo_CPF)
        return CPFs_ordenados
    
    def ordenar_CNPJs(self):
        #Passar lista os números dos CNPJs para uma lista auxiliar
        list_Aux = []
        for i in len(self.CNPJs_list):
            list_Aux.append(self.CNPJs_list[i].num_CNPJ)
        
        #Ordenar lista auxiliar
        list_Aux.sort()

        #Passar lista dos CPFs a partir da lista auxiliar 
        CNPJs_ordenados = []
        for i in len(range(self.CNPJs_list)):
            #Encontrar primeiro CNPJ
            novo_CNPJ = CNPJ
            novo_CNPJ = self.encontrar_CNPJ(list_Aux[i])
            
            #Passar novo CNPJ para a lista de CNPJS ordenados            
            CNPJs_ordenados.append(novo_CNPJ)
        return CNPJs_ordenados

    def ordenar_Agenda(self):
        agenda_ordenada = []
        cpfs_ordenados = self.ordenar_CPFs(self.CPFs_list)
        cnpj_ordenados = self.ordenar_CNPJs(self.CNPJs_list)
        agenda_ordenada.append(cpfs_ordenados)
        agenda_ordenada.append(cnpj_ordenados)
        return agenda_ordenada

    def __str__(self):
        string_final = "\t========== Agenda ==========\n"
        Agenda_ordenada = []
        Agenda_ordenada = self.ordenar_Agenda()
        for i in range(len(Agenda_ordenada)):
            string_final += str(Agenda_ordenada[i])
        string_final += "\t============================\n\n"
        return string_final
