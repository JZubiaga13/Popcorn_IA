import os
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar conexión a MySQL en AWS
DATABASE_URL = "mysql+pymysql://admin:jzd13051998@popcorn-db.cleardeck8ywvw.us-east-1.rds.amazonaws.com/popcorn-db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definir modelo de tabla para almacenar interacciones
class Interaction(Base):
    __tablename__ = "interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(Text)  # Películas introducidas o pregunta de trivia
    response = Column(Text)  # Recomendaciones o respuesta correcta
    interaction_type = Column(String(20))  # "recommendation" o "trivia"
    user_answer = Column(Text, nullable=True)  # Respuesta del usuario en trivia

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)
