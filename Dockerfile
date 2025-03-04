# Usa la imagen oficial de Python como base
FROM python:3.11

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos e instalarlos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al contenedor
COPY . .

# Exponer los puertos para FastAPI (8000) y Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Definir el comando de inicio
CMD ["sh", "-c", "uvicorn app.popcorn:app --host 0.0.0.0 --port 8000 & streamlit run app/frontend.py --server.port 8501 --server.address 0.0.0.0"]
