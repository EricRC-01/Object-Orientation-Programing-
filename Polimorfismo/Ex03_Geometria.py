# Geometria


class figura_geometrica:
    qnt_lados = 0
    area = 0
    perimetro = 0
    cor = str
    #define se a figura esta preenchida (1) ou se não (0)
    filled = -1 

    def calc_perimetro(self):
        pass        
    def calc_area(self):
        pass

class retangulo(figura_geometrica):
    base = 0
    altura = 0    

    def calc_area(self):
        return (self.altura * self.base)
    def calc_perimetro(self):
        return( (self.base*2)+(self.altura*2) )

    def __init__(self, altura, base, cor):
        if(cor == "Vazio"):
            filled = 0
        else: 
            self.cor = cor
            self.filled = 1
        self.qnt_lados = 4
        self.altura = altura
        self.base = base 
        
        self.area = self.calc_area()
        self.perimetro = self.calc_perimetro()

class quadrado(retangulo):
    def __init__(self, valor_lado, cor):
        if(cor == "Vazio"):
            self.filled = 0
        else: self.cor = cor
        self.altura = valor_lado
        self.base = self.altura

#Considerando pi = 3,14
class circulo(figura_geometrica):
    raio = 0
    
    def calc_area(self):
        return (3,14 * ((self.raio)*(self.raio)))
    def calc_perimetro(self):
        return (2*3,14*(self.raio))
    
    def __init__(self, raio, cor):
        if(cor == "Vazio"):
            filled = 0
        else: 
            self.cor = cor
            self.filled = 1
        
        #Como colocar infinito ???
        self.qnt_lados = -1
        self.raio = raio
        self.area = self.calc_area()
        self.perimetro = self.calc_perimetro()
        
        

    
        