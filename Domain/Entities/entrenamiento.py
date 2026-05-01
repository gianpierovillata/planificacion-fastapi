class entrenamiento:


    #propiedades
    id_entrenamiento:int
    ejercicio:str
    duracion:str

    def __init__(self, id_entrenamiento:int, ejercicio:str, duracion:str):
        self.id_entrenamiento=id_entrenamiento
        self.ejercicio=ejercicio
        self.duracion=duracion