from pydantic import BaseModel
from typing import List

class MovieInput(BaseModel):
    favorites: List[str]

class MovieRecommendation(BaseModel):
    recommendations: List[str]

class TriviaRequest(BaseModel):
    category: str  # "movies", "series", "both"

class TriviaResponse(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
