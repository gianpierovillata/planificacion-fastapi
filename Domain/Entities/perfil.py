class perfil:

    #propiedades
    id_perfil:int
    id_atleta:int
    objetivos:str

    def __init__(self, id_perfil:int, id_atleta:int, objetivos:str):
        self.id_perfil=id_perfil
        self.id_atleta=id_atleta
        self.objetivos=objetivos