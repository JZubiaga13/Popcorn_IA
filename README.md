# POPCORN_AI
# Recomendador de Películas & Trivia de Cine/Series con IA

**Popcorn AI** es una plataforma basada en IA generativa que ofrece:
- Un **Recomendador de Películas**, que sugiere títulos similares según los gustos del usuario.
- Un **Trivia de Cine y Series**, donde los usuarios pueden responder preguntas con cuatro opciones.

Desarrollado con **FastAPI, OpenAI, AWS y Docker**.

---

## 🚀 Características
✅ **Recomendador de Películas**: Introduce varias películas y obtén recomendaciones similares.  
✅ **Trivia de Cine y Series**: Preguntas generadas con IA y opciones de respuesta.  
✅ **Base de Datos en AWS**: Registro de consultas, respuestas y recomendaciones.  
✅ **Visualización en Web**: Interfaz HTML o Streamlit.  
✅ **Dockerizado y Desplegable**: Contenedor listo para implementación.  

---

## 📂 Estructura del Proyecto
```
📁 popcorn_ai/
│── 📁 app/                 # Código de la aplicación
│   │── 📄 main.py          # API con FastAPI
│   │── 📄 models.py        # Integración con OpenAI
│   │── 📄 database.py      # Conexión con PostgreSQL en AWS
│   │── 📄 schemas.py       # Esquema de datos (Pydantic)
│   │── 📄 frontend.py      # (Si se usa Streamlit)
│── 📁 templates/           # HTML (Si no se usa Streamlit)
│   │── 📄 index.html       # Página principal
│   │── 📄 trivia.html      # Trivia UI
│   │── 📄 recomendador.html # Recomendador UI
│── 📁 static/              # Archivos CSS, JS, imágenes
│── 📁 tests/               # Pruebas unitarias
│── 📄 Dockerfile           # Dockerización
│── 📄 requirements.txt     # Dependencias
│── 📄 README.md            # Documentación del proyecto
```

---

## 🛠 Instalación y Configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/popcorn_ai.git
cd popcorn_ai
```

### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Configurar variables de entorno
Crear un archivo **.env** con las credenciales de OpenAI y AWS:
```env
OPENAI_API_KEY=tu_clave_de_openai
DATABASE_URL=postgresql://usuario:contraseña@tu-rds.amazonaws.com/dbname
```

### 4️⃣ Ejecutar la aplicación
```bash
uvicorn app.main:app --reload
```
Acceder en: `http://127.0.0.1:8000/docs` 📜

---

## 🐳 Dockerización
### 1️⃣ Construir y ejecutar la imagen Docker
```bash
docker build -t popcorn_ai .
docker run -p 8000:8000 popcorn_ai
```

### 2️⃣ Subir imagen a DockerHub
```bash
docker tag popcorn_ai tu_usuario/popcorn_ai
docker push tu_usuario/popcorn_ai
```

---

## ☁️ Despliegue en AWS
- **Base de Datos:** PostgreSQL en AWS RDS.
- **Servidor:** Opcionalmente, desplegar en EC2 o servicios como Railway.app.

---

## 📜 Endpoints Principales
| Método | Endpoint        | Descripción |
|---------|----------------|-------------|
| `POST`  | `/recommend`   | Recomendador de películas |
| `GET`   | `/trivia`      | Generador de preguntas de trivia |
| `POST`  | `/save_interaction` | Guarda consultas y respuestas |
| `POST`  | `/save_trivia` | Guarda preguntas en BD |

---

## 📝 Contribuciones
1. **Fork** este repositorio.
2. Crea una rama: `git checkout -b feature-nueva`.
3. Sube tus cambios: `git push origin feature-nueva`.
4. Abre un Pull Request.

---

## 📌 Autor
**[Tu Nombre]** - [Tu Usuario de GitHub]  
💡 Inspirado en la IA aplicada al entretenimiento 🎬📺

