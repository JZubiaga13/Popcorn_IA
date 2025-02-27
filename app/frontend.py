import streamlit as st
import requests

# Configurar la página con icono y título
st.set_page_config(page_title="Popcorn AI", page_icon="🍿", layout="centered")

# Definir la URL base de la API
API_URL = "http://127.0.0.1:8000"

# Estilo CSS con HTML inyectado en Streamlit
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff6600;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            font-weight: normal;
            color: #444;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .button-container button {
            background-color: #ff6600;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
        }
        .button-container button:hover {
            background-color: #cc5500;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado con HTML
st.markdown("<h1 class='title'>🍿 Popcorn AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Recomendador de Películas y Trivia de Cine/Series</p>", unsafe_allow_html=True)

# Contenedor para los botones de selección
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 Recomendador de Películas"):
        st.session_state["option"] = "recomendador"

with col2:
    if st.button("🎥 Trivia de Cine y Series"):
        st.session_state["option"] = "trivia"

st.markdown("</div>", unsafe_allow_html=True)

# Verificar qué opción eligió el usuario
if "option" in st.session_state:
    option = st.session_state["option"]

    if option == "recomendador":
        st.subheader("🎬 Ingresa películas que te gusten")
        favorites = st.text_input("Escribe algunas películas separadas por comas:")

        if st.button("Obtener Recomendaciones"):
            if favorites:
                payload = {"favorites": [fav.strip() for fav in favorites.split(",")]}
                response = requests.post(f"{API_URL}/recommend", json=payload)

                if response.status_code == 200:
                    st.success("¡Aquí están tus recomendaciones!")
                    st.write(response.json()["recommendations"])
                else:
                    st.error("Error al obtener recomendaciones")

    elif option == "trivia":
        st.subheader("🎥 Juega una trivia de cine o series")

        if st.button("Generar Pregunta"):
            response = requests.get(f"{API_URL}/trivia")

            if response.status_code == 200:
                trivia = response.json()
                st.write(f"**Pregunta:** {trivia['question']}")

                correct_answer = trivia["correct_answer"]
                opciones = trivia["options"]
                chosen = st.radio("Selecciona una respuesta:", opciones)

                if st.button("Comprobar Respuesta"):
                    if chosen == correct_answer:
                        st.success("✅ ¡Correcto!")
                    else:
                        st.error(f"❌ Incorrecto. La respuesta correcta es: {correct_answer}")
            else:
                st.error("Error al obtener la trivia")
