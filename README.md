# API de Planificación Deportiva

API para gestionar planes de entrenamiento y perfiles de atletas, construida con **FastAPI**.

## Stack Tecnológico

- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn + Gunicorn
- **Validación:** Pydantic
- **Deploy:** Render

## Requisitos

- Python 3.13+
- Ver `requirements.txt`

## Instalación Local

```bash
git clone <repo-url>
cd planificacion
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar Localmente

```bash
uvicorn main:app --reload
```

Abre en el navegador:
- **API:** http://localhost:8000
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Bienvenida |
| GET | `/saludar` | Saludo |
| GET | `/atleta` | Obtener atleta |
| GET | `/perfil/{id_atleta}` | Obtener perfil de atleta |
| GET | `/plan/{id}` | Obtener plan |

## Deploy en Render

1. Crea un nuevo **Web Service** en [Render](https://render.com) conectando tu repositorio.
2. Configura los siguientes campos:

| Campo | Valor |
|-------|-------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -k uvicorn.workers.UvicornWorker main:app` |

3. El `requirements.txt` ya contiene las dependencias mínimas necesarias:
   - `fastapi`
   - `uvicorn`
   - `gunicorn`

4. Haz clic en **Create Web Service**. Render detectará el puerto automáticamente.

## Estructura del Proyecto

```
planificacion/
├── main.py              # Punto de entrada de la API
├── requirements.txt     # Dependencias
└── README.md
```
