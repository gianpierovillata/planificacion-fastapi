from fastapi import FastAPI, APIRouter

app= FastAPI()

app.title = "API de Planificacion Deportiva"
app.description = "API para gestionar planes de entrenamiento y perfiles de atletas"
app.version = "1.0.0"
app.contact = {
    "name": "Piero",
    "email": "piero@example.com"}   

app.license_info = {    

    "name": "MIT License",
    "url": "https://opensource.org/licenses/MIT"
}
app.openapi_tags=[
    {"name":"Bienvenida", "description":"Operaciones relacionadas con la bienvenida a la API"},
    {"name":"Atleta", "description":"Operaciones relacionadas con atletas"},
    {"name":"Plan", "description":"Operaciones relacionadas con planes de entrenamiento"},
    {"name":"Perfil", "description":"Operaciones relacionadas con perfiles de atletas"},
    {"name":"Entrenamiento", "description":"Operaciones relacionadas con entrenamientos"}

]
# Definir rutas de la API
general_router = APIRouter(tags=["Bienvenida"])
atleta_router = APIRouter(tags=["Atleta"])
plan_router = APIRouter(tags=["Plan"])
perfil_router = APIRouter(tags=["Perfil"])
entrenamiento_router = APIRouter(tags=["Entrenamiento"])

@general_router.get("/")
def bienvenida():
    return {"Bienvenida a API de Planificacion Deportiva en Python FASTAPI"}


@general_router.get("/saludar")
def saludar():
    return "Bienvenido campeon"

@atleta_router.get("/atleta")
def get_atleta():
    atleta ={"nombre":"Piero","edad":42}
    return atleta

@plan_router.get("/plan/{id}")
def get_plan(id:int):
    return {"num":id,"nombre":"Plan inicial"}

@perfil_router.get("/perfil/{id_atleta}")
def get_perfil(id_atleta:int):
    atleta={"id":id_atleta, "nombre":"Atleta Uno", "categoria":"Junior"}
    return atleta

@entrenamiento_router.get("/entrenamiento/{id_plan}")
def get_entrenamiento(id_plan:int):
    entrenamiento={"id":id_plan, "ejercicio":"Correr", "duracion":"30 minutos"}
    return entrenamiento

@entrenamiento_router.get("/entrenamientos")
def get_entrenamientos():
    entrenamientos =[{"id":1,"ejercicio":"Nadar","tiempo":3,"kilometros":2.5}]
    return entrenamientos

# Incluir routers en la aplicación principal
app.include_router(general_router)
app.include_router(atleta_router)
app.include_router(plan_router)
app.include_router(perfil_router)
app.include_router(entrenamiento_router)



