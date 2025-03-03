from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import pymysql
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate

app = FastAPI()

class Consultas(BaseModel):
    peliculas: list[str] | None = None  # Lista opcional de películas
    contexto: str | None = None  # Contexto opcional

# Cargar las variables de entorno
load_dotenv()

# Obtener datos de la base de datos
user = os.getenv('user')
password = os.getenv('password_db')
host = os.getenv('Database_URL')
api_key = os.getenv('cohere_api')

# Verificar que la API key de Cohere se ha cargado correctamente
if not api_key:
    raise ValueError("API Key de Cohere no encontrada. Verifica el archivo .env")

# Configuración correcta de Cohere en LangChain
llm = ChatCohere(cohere_api_key=api_key)

# Definir una plantilla de prompt flexible para películas y contexto
prompt = PromptTemplate(
    input_variables=["peliculas", "contexto"],
    template="Dame 5 películas populares similares a {peliculas} "
             "o recomendadas para {contexto}. Explica brevemente por qué."
)
# prompt = PromptTemplate(
#     input_variables=["peliculas"],
#     template="Dame 5 películas populares similares a {peliculas} y explica brevemente por qué."
# )

# Definir el pipeline de generación de texto
recomendacion_chain = prompt | llm

@app.get("/")
async def hola():
    return {"Bienvenido a PopcornIA"}

@app.post("/recomendacion")
async def recomienda(pregunta: Consultas):
    try:
        # Construir la consulta según lo que haya ingresado el usuario
        peliculas_texto = ", ".join(pregunta.peliculas) if pregunta.peliculas else "ninguna en particular"
        contexto_texto = pregunta.contexto if pregunta.contexto else "sin un contexto específico"

        consulta_final = f"{peliculas_texto} | {contexto_texto}"

        # Generar respuesta con LangChain
        raw_response = recomendacion_chain.invoke({"peliculas": peliculas_texto, "contexto": contexto_texto})
        response = raw_response.content  # Extraer solo el contenido del mensaje

        # Conectar a la base de datos y guardar la interacción
        db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database="popcorn_db",
            cursorclass=pymysql.cursors.DictCursor
        )

        cursor = db.cursor()
        query = "INSERT INTO interactions (pregunta, respuesta) VALUES (%s, %s)"
        cursor.execute(query, (consulta_final, response))
        db.commit()
        cursor.close()
        db.close()

        return {"respuesta": response}
    
    except Exception as e:
        return {"error": str(e)}


# PRUEBA SIN CONTEXTO
# @app.post("/recomendacion")
# async def recomienda(pregunta: Consultas):
#     try:
#         # Generar respuesta con LangChain
#         raw_response = recomendacion_chain.invoke(pregunta.consultas)  # Respuesta completa
#         response = raw_response.content  # Extraer solo el contenido del mensaje

#         # Conectar a la base de datos
#         db = pymysql.connect(
#             host=host,
#             user=user,
#             password=password,
#             database="popcorn_db",
#             cursorclass=pymysql.cursors.DictCursor
#         )

#         cursor = db.cursor()
#         query = "INSERT INTO interactions (pregunta, respuesta) VALUES (%s, %s)"
#         cursor.execute(query, (pregunta.consultas, response))
#         db.commit()
#         cursor.close()
#         db.close()

#         return {"respuesta": response}
    
#     except Exception as e:
#         return {"error": str(e)}


# PRUEBA ANTERIOR SIN LANGCHAIN
# @app.get("/")
# async def hola():
#     return {"Bienvenido a PopcornIA"}

# # Endpoint para obtener recomendaciones
# @app.post("/recomendacion")
# async def recomienda(pregunta: Consultas):  # Asegurar que pregunta es de tipo Consultas
#     co = cohere.ClientV2(api_key)
#     response = co.chat(
#         model="command-r-plus",
#         messages=[{"role": "system", "content": "Eres un aficionado al cine y quieres que te recomienden películas"},
#                   {"role": "user", "content": pregunta.consultas}]
    # )






# uvicorn.run(app)






# **CODIGO DE DEEPSEEK**

# from app.database import SessionLocal, Interaction
# from app.schemas import MovieInput, MovieRecommendation, TriviaResponse
# from app.models import get_recommendations, generate_trivia

# # Dependencia para obtener la sesión de la base de datos
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Endpoint para recomendaciones de películas
# @app.post("/recommend", response_model=MovieRecommendation)
# def recommend_movies(user_input: MovieInput, db: Session = Depends(get_db)):
#     recommendations = get_recommendations(user_input.favorites)
#     return {"recommendations": recommendations}

# # Endpoint para trivia de cine y series
# @app.get("/trivia", response_model=TriviaResponse)
# def get_trivia(db: Session = Depends(get_db)):
#     trivia = generate_trivia()
#     return trivia

# # Endpoint para obtener historial de interacciones
# @app.get("/history")
# def get_history(db: Session = Depends(get_db)):
#     interactions = db.query(Interaction).all()
#     return [{"id": i.id, "input": i.user_input, "response": i.response, "type": i.interaction_type} for i in interactions]