from .atleta import atleta
class plan:

    #propiedades
    id_plan:int
    atlea:atleta
    nombre:str
    descripcion:str
    entrenamientos:list

    
    def __init__(self,id_plan:int, nombre:str, descripcion:str):
        self.id_plan=id_plan
        self.nombre=nombre
        self.descripcion=descripcion
        self.entrenamientos=[]