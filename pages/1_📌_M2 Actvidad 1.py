import streamlit as st
import pandas as pd

st.set_page_config(page_icon="🎮", layout="wide")
st.title("Actividad 1 - Videojuegos")
st.header("Descripción")
st.markdown("Esta actividad muestra cómo crear un DataFrame a partir de un diccionario con información de videojuegos y cómo visualizar tanto los datos como las secciones importantes del código.")

videojuegos = {
    "Título": ["The Legend of Zelda", "Super Mario Odyssey", "God of War", "Red Dead Redemption 2"],
    "Plataforma": ["Nintendo Switch", "Nintendo Switch", "PlayStation 4", "PlayStation 4"],
    "Año": [2017, 2017, 2018, 2018],
    "Desarrollador": ["Nintendo", "Nintendo", "Santa Monica Studio", "Rockstar Games"]
}
df_videojuegos = pd.DataFrame(videojuegos)
st.subheader("DataFrame de Videojuegos")
st.dataframe(df_videojuegos)

codigo = '''
import streamlit as st
import pandas as pd

st.set_page_config(page_icon="🎮", layout="wide")
st.title("Actividad 1 - Videojuegos")
st.header("Descripción")
st.markdown("Esta actividad muestra cómo crear un DataFrame a partir de un diccionario con información de videojuegos y cómo visualizar tanto los datos como las secciones importantes del código.")

videojuegos = {
    "Título": ["The Legend of Zelda", "Super Mario Odyssey", "God of War", "Red Dead Redemption 2"],
    "Plataforma": ["Nintendo Switch", "Nintendo Switch", "PlayStation 4", "PlayStation 4"],
    "Año": [2017, 2017, 2018, 2018],
    "Desarrollador": ["Nintendo", "Nintendo", "Santa Monica Studio", "Rockstar Games"]
}
df_videojuegos = pd.DataFrame(videojuegos)
st.subheader("DataFrame de Videojuegos")
st.dataframe(df_videojuegos)
'''
st.subheader("Código")
st.code(codigo, language="python")
