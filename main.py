from fastapi import FastAPI

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

@app.get("/")
def bienvenida():
    return {"Bienvenida a API de Planificacion Deportiva en Python FASTAPI"}


@app.get("/saludar")
def saludar():
    return "Bienvenido campeon"

@app.get("/atleta")
def get_atleta():
    atleta ={"nombre":"Piero","edad":42}
    return atleta

@app.get("/plan/{id}")
def get_plan(id:int):
    return {"num":id,"nombre":"Plan inicial"}

@app.get("/perfil/{id_atleta}")
def get_perfil(id_atleta:int):
    atleta={"id":id_atleta, "nombre":"Atleta Uno", "categoria":"Junior"}
    return atleta
