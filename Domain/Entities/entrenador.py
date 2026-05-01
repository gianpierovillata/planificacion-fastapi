class entrenador:
    
    #propiedades
    id_entrenador:int
    nombre:str
    especialidad:str
    planes_entrenamiento:list

    def __init__(self, id_entrenador:int, nombre:str, especialidad:str):
        self.id_entrenador=id_entrenador
        self.nombre=nombre
        self.especialidad=especialidad
        self.planes_entrenamiento=[]