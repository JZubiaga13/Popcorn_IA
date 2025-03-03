import openai
import os
import requests
from dotenv import load_dotenv
from app.database import SessionLocal, Interaction

# Cargar API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener recomendaciones de películas y guardarlas
def get_recommendations(favorites):
    prompt = f"Dame 5 películas populares similares a: {', '.join(favorites)}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    recommendations = response["choices"][0]["message"]["content"].split("\n")[:5]

    # Guardar en la base de datos
    db = SessionLocal()
    new_entry = Interaction(
        user_input=", ".join(favorites),
        response=", ".join(recommendations),
        interaction_type="recommendation"
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    db.close()

    return recommendations

# Función para obtener preguntas de trivia desde OpenTriviaDB y guardarlas
def generate_trivia():
    url = "https://opentdb.com/api.php?amount=1&category=11&type=multiple"
    response = requests.get(url).json()
    
    if response["response_code"] == 0:
        question_data = response["results"][0]
        question = question_data["question"]
        correct_answer = question_data["correct_answer"]
        options = question_data["incorrect_answers"] + [correct_answer]
        
        # Mezclar opciones aleatoriamente
        import random
        random.shuffle(options)

        # Guardar en la base de datos
        db = SessionLocal()
        new_entry = Interaction(
            user_input=question,
            response=correct_answer,
            interaction_type="trivia"
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        db.close()

        return {"question": question, "options": options, "correct_answer": correct_answer}
    else:
        return {"error": "No se pudieron obtener preguntas en este momento"}
