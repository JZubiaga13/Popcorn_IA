# 🎬 **Popcorn-IA** 🍿

*"¿Alguna vez has pasado más tiempo eligiendo qué ver que viendo la película? Entonces, esto es para ti."*

## 🎭 **¿Qué es PopcornIA?**

**Popcorn-IA** es un recomendador de películas inteligente que utiliza **Inteligencia Artificial y Procesamiento del Lenguaje Natural (NLP)** para sugerirte películas según **tus gustos o el contexto en el que te encuentres**.\
🔹 ¿Buscas una peli para ver con amigos? 🎉\
🔹 ¿Algo inspirador como *Interestelar*? 🚀\
🔹 ¿O quizás un thriller tipo *Joker*? 🎭

Solo dinos lo que te gusta o el ambiente en el que te encuentras, y **Popcorn-IA** hará el resto.

---

## 📚 **Estructura del Proyecto**

Popcorn_IA/
│── app/   
│   ├── __init__.py  ––            Inicialización del módulo   
│   ├── frontend.py  ––            Interfaz Streamlit   
│   ├── popcorn.py  ––             API con FastAPI   
│   
│── tests/   
│   ├── pytest_cache/ ––           Caché de pytest   
│   ├── pytest.ini  ––              Configuración de pytest   
│   ├── test_popcorn.py  ––        # Tests automatizados   
│   
│── .dockerignore  ––              # Archivos ignorados por Docker   
│── .gitignore  –                # Archivos ignorados en Git   
│── Dockerfile  –                # Configuración de Docker   
│── README.md  –                 # Documentación del proyecto   
│── requirements.txt  –            # Dependencias del proyecto   


## 🚀 **Instalación y Ejecución**

### 🔹 **Opción 1: Ejecutar con Docker** (recomendada)

Si quieres usar **Popcorn-IA** sin instalar dependencias manualmente:

```bash
docker pull juanzubiaga/popcornia:latest
docker run -p 8000:8000 -p 8501:8501 juanzubiaga/popcornia:latest
```

Luego accede a:\
🔗 **API:** `http://127.0.0.1:8000/docs`\
🔗 **Interfaz Web:** `http://127.0.0.1:8501`

### 🔹 **Opción 2: Ejecutar localmente**

1️⃣ **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/Popcorn-IA.git
cd Popcorn-IA
```

2️⃣ **Configurar las variables de entorno**\
Renombra `.env.example` a `.env` y completa los valores necesarios:

```ini
user=tu_usuario_mysql
password_db=tu_password_mysql
Database_URL=tu_host_mysql
cohere_api=tu_api_key_cohere
```

3️⃣ **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4️⃣ **Ejecutar el backend y la interfaz**

```bash
uvicorn app.popcorn:app --host 0.0.0.0 --port 8000 --reload  # API FastAPI
streamlit run app/frontend.py  # Interfaz Web
```

---

## 🛋 **Dependencias (requirements.txt)**

Este proyecto usa las siguientes librerías:

```
fastapi
uvicorn
pydantic
cohere
langchain
langchain-cohere
streamlit
pytest
pymysql
python-dotenv
```

Para instalarlas manualmente:

```bash
pip install -r requirements.txt
```

---

## 🧪 **Pruebas**

Para ejecutar los tests con **pytest**:

```bash
pytest tests/
```

---

Porque al igual que **Tony Stark confiaba en J.A.R.V.I.S.**, o **Neo en Morfeo**, Popcorn-IA te ayuda a elegir sin caer en la parálisis por análisis.

---

## 🎯 **Futuro Desarrollo**

📌 **Mejora de recomendaciones** con modelos avanzados de IA.\
📌 **Implementación de Trivia de Cine y Series.**\
📌 **Despliegue en la nube para acceso global.**

---

## 🐝 **Licencia**

Este proyecto es de código abierto bajo la licencia **MIT**.


*"No importa la película que elijas, lo importante es compartirla con alguien."* 🍿

