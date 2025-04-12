# Importar bibliotecas necesarias
import pandas as pd
import numpy as np
from faker import Faker
import random
import streamlit as st
from datetime import datetime

st.markdown("[Enlace a mi cuaderno de  Google Colab para la Actividad 1](https://colab.research.google.com/drive/1V2msmhoh8roK-69M1yiMxrV6CUPQQJj1?usp=sharing)"
)
# Configurar Faker para Colombia
fake = Faker('es_CO')

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos para el DataFrame
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',
            'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal',
            'Leticia', 'Puerto Inírida'
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

# Convertir fecha_nacimiento a datetime
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

# Configurar título de la aplicación
st.title("Aplicación de Filtros Dinámicos con Streamlit")

# Crear sección de filtros en la parte superior
with st.expander("Filtros Dinámicos"):
    # Inicializar DataFrame filtrado
    df_filtrado = df_nuevo.copy()

    # 1. Filtro por rango de edad (usando between)
    if st.checkbox("Filtrar por rango de edad"):
        min_edad, max_edad = st.slider(
            "Selecciona el rango de edad",
            min_value=15,
            max_value=75,
            value=(15, 75)
        )
        df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

    # 2. Filtro por municipios específicos (usando isin)
    if st.checkbox("Filtrar por municipios"):
        municipios = [
            'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín',
            'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
        ]
        municipios_seleccionados = st.multiselect(
            "Selecciona municipios",
            options=municipios,
            default=[]
        )
        if municipios_seleccionados:
            df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

    # 3. Filtro por ingreso mensual mínimo (usando operador >)
    if st.checkbox("Filtrar por ingreso mensual mínimo"):
        ingreso_minimo = st.slider(
            "Selecciona ingreso mínimo (COP)",
            min_value=800000,
            max_value=12000000,
            value=800000,
            step=100000
        )
        df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

    # 4. Filtro por ocupación (usando isin)
    if st.checkbox("Filtrar por ocupación"):
        ocupaciones = [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero',
            'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero'
        ]
        ocupaciones_seleccionadas = st.multiselect(
            "Selecciona ocupaciones",
            options=ocupaciones,
            default=[]
        )
        if ocupaciones_seleccionadas:
            df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

    # 5. Filtro por tipo de vivienda no propia (usando operador != y ~)
    if st.checkbox("Filtrar personas sin vivienda propia"):
        df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

    # 6. Filtro por nombres que contienen una cadena (usando str.contains)
    if st.checkbox("Filtrar por nombre"):
        texto = st.text_input("Ingresa texto para buscar en el nombre", value="")
        if texto:
            df_filtrado = df_filtrado[
                df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)
            ]

    # 7. Filtro por año de nacimiento específico (usando fechas)
    if st.checkbox("Filtrar por año de nacimiento"):
        años = list(range(1949, 2010))
        año_seleccionado = st.selectbox(
            "Selecciona el año de nacimiento",
            options=años
        )
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año_seleccionado]

    # 8. Filtro por acceso a internet (usando operador ==)
    if st.checkbox("Filtrar por acceso a internet"):
        acceso = st.radio(
            "Selecciona acceso a internet",
            options=["Sí", "No"]
        )
        df_filtrado = df_filtrado[
            df_filtrado['acceso_internet'] == (acceso == "Sí")
        ]

    # 9. Filtro por ingresos nulos (usando isnull)
    if st.checkbox("Filtrar por ingresos nulos"):
        df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

    # 10. Filtro por rango de fechas de nacimiento (usando between)
    if st.checkbox("Filtrar por rango de fechas de nacimiento"):
        fecha_inicio = st.date_input(
            "Fecha inicial",
            value=datetime(1949, 1, 1),
            min_value=datetime(1949, 1, 1),
            max_value=datetime(2009, 12, 31)
        )
        fecha_fin = st.date_input(
            "Fecha final",
            value=datetime(2009, 12, 31),
            min_value=datetime(1949, 1, 1),
            max_value=datetime(2009, 12, 31)
        )
        df_filtrado = df_filtrado[
            df_filtrado['fecha_nacimiento'].between(
                pd.to_datetime(fecha_inicio),
                pd.to_datetime(fecha_fin)
            )
        ]

# Mostrar el DataFrame filtrado
st.write("### Datos Filtrados")
st.dataframe(df_filtrado)

# Mostrar información adicional
st.write(f"**Número de registros después de aplicar filtros:** {len(df_filtrado)}")