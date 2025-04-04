import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# Configuración inicial de la página
st.set_page_config(page_icon="🎮", layout="wide")
st.title("Actividad 1 - Creación de DataFrames sobre Videojuegos")
st.markdown("Esta actividad muestra cómo crear DataFrames en Pandas a partir de diferentes fuentes de datos relacionadas con videojuegos y visualizarlos en Streamlit.")

# 1. Diccionario
st.subheader("DataFrame desde Diccionario")
videojuegos_dict = {
    "Título": ["The Legend of Zelda", "Super Mario Odyssey", "God of War", "Red Dead Redemption 2"],
    "Plataforma": ["Nintendo Switch", "Nintendo Switch", "PlayStation 4", "PlayStation 4"],
    "Año": [2017, 2017, 2018, 2018],
    "Desarrollador": ["Nintendo", "Nintendo", "Santa Monica Studio", "Rockstar Games"]
}
df_dict = pd.DataFrame(videojuegos_dict)
st.dataframe(df_dict)

# 2. Lista de diccionarios
st.subheader("DataFrame desde Lista de Diccionarios")
videojuegos_list_dict = [
    {"Título": "Hollow Knight", "Género": "Metroidvania", "Ventas (millones)": 2.8},
    {"Título": "Stardew Valley", "Género": "Simulación", "Ventas (millones)": 20.0},
    {"Título": "Celeste", "Género": "Plataformas", "Ventas (millones)": 1.0}
]
df_list_dict = pd.DataFrame(videojuegos_list_dict)
st.dataframe(df_list_dict)

# 3. Lista de listas
st.subheader("DataFrame desde Lista de Listas")
videojuegos_list = [
    ["Minecraft", 29.99, 238],
    ["GTA V", 59.99, 185],
    ["Tetris", 4.99, 170]
]
df_list = pd.DataFrame(videojuegos_list, columns=["Título", "Precio (USD)", "Ventas (millones)"])
st.dataframe(df_list)

# 4. Series
st.subheader("DataFrame desde Series")
titulos = pd.Series(["Persona 5", "Overwatch", "Among Us"])
plataformas = pd.Series(["PlayStation 4", "PC", "Multiplataforma"])
calificaciones = pd.Series([9.3, 8.5, 7.8])
df_series = pd.DataFrame({"Título": titulos, "Plataforma": plataformas, "Calificación": calificaciones})
st.dataframe(df_series)

# 5. Archivo CSV (local) - 
st.subheader("DataFrame desde CSV")
df_csv = pd.read_csv("data/videojuegos.csv")
st.dataframe(df_csv)

# 6. Archivo Excel (local) - 
st.subheader("DataFrame desde Excel")
df_excel = pd.read_excel("data/videojuegos.xlsx") 
st.dataframe(df_excel)

# 7. Archivo JSON (local) - 
st.subheader("DataFrame desde JSON")
df_json = pd.read_json("data/videojuegos.json") 
st.dataframe(df_json)

# 8. URL
st.subheader("DataFrame desde URL")
url = "https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv"
df_url = pd.read_csv(url)
st.dataframe(df_url.head(5))  

# 9. SQLite
st.subheader("DataFrame desde SQLite")
conn = sqlite3.connect("videojuegos.db")
conn.execute("CREATE TABLE IF NOT EXISTS juegos (titulo TEXT, ano INTEGER, desarrollador TEXT)")
conn.execute("INSERT INTO juegos VALUES ('Elden Ring', 2022, 'FromSoftware'), ('Hades', 2020, 'Supergiant Games'), ('Cyberpunk 2077', 2020, 'CD Projekt')")
conn.commit()
df_sqlite = pd.read_sql("SELECT * FROM juegos", conn)
st.dataframe(df_sqlite)
conn.close()

# 10. Array de NumPy
st.subheader("DataFrame desde Array de NumPy")
ventas_np = np.array([
    [50, 30, 20],
    [80, 45, 35],
    [120, 60, 50]
])
df_numpy = pd.DataFrame(ventas_np, columns=["Ventas 2020", "Ventas 2021", "Ventas 2022"], index=["Juego A", "Juego B", "Juego C"])
st.dataframe(df_numpy)