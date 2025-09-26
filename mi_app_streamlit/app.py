import streamlit as st
from modules.utils import cargar_datos

st.title('Demo de estructura')
df = cargar_datos('data/ventas.csv')
st.dataframe(df)


valor = st.slider('Selecciona un valor', 0, 100, 50)  # Slider interactivo
resultado = valor ** 2  # Cálculo reactivo
st.write(f'El cuadrado de {valor} es {resultado}')  # Muestra el resultado

def incrementar():
    st.session_state.contador += 1  # Aumenta el contador en 1

if 'contador' not in st.session_state:
    st.session_state.contador = 0  # Inicializa el contador

st.button('Sumar', on_click=incrementar)  # Botón con callback
st.write(f'Contador: {st.session_state.contador}')  # Muestra el valor