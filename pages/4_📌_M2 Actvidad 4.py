import pandas as pd
import numpy as np
import streamlit as st

# Crear un DataFrame de ejemplo
n = 100
data = {
    'id': range(1, n + 1),
    'nombre': [f'Persona {i}' for i in range(1, n + 1)],
    'edad': np.random.randint(18, 65, n),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], n),
    'ingreso': np.random.randint(1000000, 10000000, n)
}
df = pd.DataFrame(data)

# Configurar título de la aplicación
st.title("Exploración y Manipulación de Datos con .loc y .iloc")

# Mostrar el DataFrame original
st.write("### DataFrame Original")
st.dataframe(df)

# Sección para explorar datos con .loc
st.write("## Exploración con .loc")
fila_inicio = st.number_input("Fila de inicio (loc)", min_value=0, max_value=len(df)-1, value=0)
fila_fin = st.number_input("Fila de fin (loc)", min_value=0, max_value=len(df), value=5)
columnas = st.multiselect("Selecciona columnas (loc)", options=df.columns.tolist(), default=df.columns.tolist())

if st.button("Aplicar .loc"):
    df_loc = df.loc[fila_inicio:fila_fin, columnas]
    st.write("### Resultado de .loc")
    st.dataframe(df_loc)

# Sección para explorar datos con .iloc
st.write("## Exploración con .iloc")
fila_inicio_iloc = st.number_input("Fila de inicio (iloc)", min_value=0, max_value=len(df)-1, value=0, key="iloc_start")
fila_fin_iloc = st.number_input("Fila de fin (iloc)", min_value=0, max_value=len(df), value=5, key="iloc_end")
columna_inicio_iloc = st.number_input("Columna de inicio (iloc)", min_value=0, max_value=len(df.columns)-1, value=0)
columna_fin_iloc = st.number_input("Columna de fin (iloc)", min_value=0, max_value=len(df.columns), value=len(df.columns))

if st.button("Aplicar .iloc"):
    df_iloc = df.iloc[fila_inicio_iloc:fila_fin_iloc, columna_inicio_iloc:columna_fin_iloc]
    st.write("### Resultado de .iloc")
    st.dataframe(df_iloc)

# Sección para modificar datos
st.write("## Modificación de Datos")
fila_modificar = st.number_input("Fila a modificar", min_value=0, max_value=len(df)-1, value=0, key="mod_row")
columna_modificar = st.selectbox("Columna a modificar", options=df.columns.tolist(), key="mod_col")
nuevo_valor = st.text_input("Nuevo valor", key="new_value")

if st.button("Modificar valor"):
    df.loc[fila_modificar, columna_modificar] = nuevo_valor
    st.write("### DataFrame Modificado")
    st.dataframe(df)

