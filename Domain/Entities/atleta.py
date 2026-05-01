
class atleta:

    #propiedades
    nombre:str
    edad:int
    categoria:str
    peso:float
    altura:float

    
    def __init__(self,id_atleta:int, nombre:str, edad:int, categoria:str, peso:float, altura:float):
        self.id_atleta=id_atleta
        self.nombre=nombre
        self.edad=edad
        self.categoria=categoria
        self.peso=peso
        self.altura=altura