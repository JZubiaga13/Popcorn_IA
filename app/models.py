import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener recomendaciones de películas
def get_recommendations(favorites):
    prompt = f"Dame 5 películas populares similares a: {', '.join(favorites)}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].split("\n")[:5]

# Función para generar preguntas de trivia
def generate_trivia(category):
    prompt = f"Genera una pregunta de trivia sobre {category} con cuatro opciones y la respuesta correcta."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
