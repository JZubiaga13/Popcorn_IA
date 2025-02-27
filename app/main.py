from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.schemas import MovieInput, MovieRecommendation, TriviaResponse
from app.models import get_recommendations, generate_trivia

app = FastAPI()

# Configurar Jinja2 para servir HTML (si usas HTML en vez de Streamlit)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return "Api de BS libros"
    return templates.TemplateResponse("index.html", {"request": request, "message": "¡Bienvenido a Popcorn AI!"})

# Endpoint para el recomendador de películas
@app.post("/recommend", response_model=MovieRecommendation)
def recommend_movies(user_input: MovieInput):
    recommendations = get_recommendations(user_input.favorites)
    return {"recommendations": recommendations}

# Endpoint para el trivia de cine y series
@app.get("/trivia", response_model=TriviaResponse)
def get_trivia(category: str = "movies"):
    trivia = generate_trivia(category)
    return {"question": trivia}
