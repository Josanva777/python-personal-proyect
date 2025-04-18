import streamlit as st
import pandas as pd

# Cargar el dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/estudiantes_colombia.csv")

data = load_data()

# Título de la aplicación
st.title("Análisis de Estudiantes en Colombia")

# Mostrar las primeras y últimas 5 filas
st.subheader("Primeras y Últimas 5 Filas del Dataset")
st.write("Primeras 5 filas:")
st.dataframe(data.head())
st.write("Últimas 5 filas:")
st.dataframe(data.tail())

# Mostrar resumen del dataset
st.subheader("Resumen del Dataset")
if st.checkbox("Mostrar .info()"):
    buffer = st.empty()
    data.info(buf=buffer)
    st.text(buffer._value)
if st.checkbox("Mostrar .describe()"):
    st.write(data.describe())

# Seleccionar columnas específicas
st.subheader("Seleccionar Columnas")
columns = st.multiselect("Selecciona las columnas a mostrar:", data.columns.tolist())
if columns:
    st.dataframe(data[columns])
    for column in columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            if column == "edad":
                selected_range = st.slider(f"Selecciona el rango para {column}:", min_value=0, max_value=80, value=(0, 80))
            else:
                min_val, max_val = float(data[column].min()), float(data[column].max())
                selected_range = st.slider(f"Selecciona el rango para {column}:", min_value=min_val, max_value=max_val, value=(min_val, max_val))
            data = data[(data[column] >= selected_range[0]) & (data[column] <= selected_range[1])]
    st.subheader("Datos Filtrados")
    st.dataframe(data)

# Filtrar estudiantes por promedio
st.subheader("Filtrar Estudiantes por Promedio")
min_promedio = st.slider("Selecciona el promedio mínimo:", min_value=float(data["promedio"].min()), max_value=float(data["promedio"].max()), value=float(data["promedio"].min()))
filtered_data = data[data["promedio"] >= min_promedio]
st.write(f"Estudiantes con promedio mayor o igual a {min_promedio}:")
st.dataframe(filtered_data)
