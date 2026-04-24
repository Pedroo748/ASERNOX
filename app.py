import streamlit as st
import time

# Configuración de la pestaña del navegador
st.set_page_config(page_title="Nuestra Gran Noticia", page_icon="🍼", layout="centered")

# Estilo CSS para que se vea moderno en celulares
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%);
        color: #4a4a4a;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        font-size: 18px;
    }
    h1 { color: #5D5D5D; text-align: center; font-family: 'Helvetica'; }
    p { text-align: center; font-size: 1.2rem; color: #777; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de navegación por pasos
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# PASO 1: Bienvenida
if st.session_state.paso == 1:
    st.markdown("<h1>✨ ¡Hola! ✨</h1>", unsafe_allow_html=True)
    st.write("Tenemos algo muy especial que contarte...")
    st.write("¿Estás listo para recibir una noticia increíble?")
    if st.button("ABRIR MENSAJE ✉️"):
        st.session_state.paso = 2
        st.rerun()

# PASO 2: La apuesta
elif st.session_state.paso == 2:
    st.markdown("<h1>🤔 ¿Qué crees que es?</h1>", unsafe_allow_html=True)
    st.write("Antes de la gran revelación, haznos saber tu apuesta:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💙 TEAM NIÑO"):
            st.session_state.voto = "un Niño 👦"
            st.session_state.paso = 3
            st.rerun()
    with col2:
        if st.button("💖 TEAM NIÑA"):
            st.session_state.voto = "una Niña 👧"
            st.session_state.paso = 3
            st.rerun()

# PASO 3: Revelación Final
elif st.session_state.paso == 3:
    st.markdown(f"<h3>Tu corazón decía que sería {st.session_state.voto}...</h3>", unsafe_allow_html=True)
    st.write("¡Llegó el momento de la verdad!")
    
    if st.button("🌟 REVELAR AHORA 🌟"):
        # Cuenta regresiva emocionante
        placeholder = st.empty()
        for i in range(3, 0, -1):
            placeholder.markdown(f"<h1 style='font-size: 100px;'>{i}</h1>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()
        
        # EFECTO FINAL (Cambia a NIÑO si es el caso)
        st.balloons()
        st.markdown("<h1 style='color: #FFB6C1; font-size: 60px;'>¡ES UNA NIÑA! 🎀</h1>", unsafe_allow_html=True)
        
        st.divider()
        st.success("📍 Te esperamos en nuestro Baby Shower")
        st.info("📅 Fecha: 20 de Junio | ⏰ Hora: 17:00 hrs | 🏠 Lugar: Nuestra casa")
