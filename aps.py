

import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="El Gran Misterio...", page_icon="🤫", layout="centered")

# 2. CSS AVANZADO (Mantenemos el diseño Premium)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .block-container {
        background-color: #ffffff;
        padding: 40px !important;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-top: 50px;
    }
    h1 { color: #2c3e50; text-align: center; font-family: 'Helvetica Neue', sans-serif; font-weight: 800; }
    h3 { color: #7f8c8d; text-align: center; font-weight: 400; }
    p { text-align: center; color: #7f8c8d; font-size: 1.1rem; }
    
    div.stButton > button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(135deg, #A9C9FF 0%, #FFBBEC 100%);
        color: white !important;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        font-size: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    .misterio-final {
        font-size: 40px !important;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(#9D50BB, #6E48AA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Control de Estado
if 'paso' not in st.session_state:
    st.session_state.paso = 1

def avanzar_paso(nuevo_paso):
    st.session_state.paso = nuevo_paso
    st.rerun()

# 4. FLUJO DINÁMICO E INCÓGNITO
# -----------------------------------

# PASO 1: EL MENSAJE INICIAL
if st.session_state.paso == 1:
    st.markdown("<h1>🤫 Un secreto está bien guardado...</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 100px; text-align: center; margin-top: -20px;'>🔐</p>", unsafe_allow_html=True)
    st.markdown("<h3>Alguien está en camino, pero su identidad es un misterio.</h3>", unsafe_allow_html=True)
    st.write("  ")
    if st.button("DESCIFRAR EL MISTERIO 🔍"):
        avanzar_paso(2)

# PASO 2: MINI-TEST INTERACTIVO
elif st.session_state.paso == 2:
    st.markdown("<h1>✨ Detector de Mitos ✨</h1>", unsafe_allow_html=True)
    st.write("Ayúdanos a analizar las pistas antes de votar.")
    
    st.markdown("**1. ¿Qué antojos ha habido más últimamente?**")
    antojo = st.radio("", ["Dulces (Chocolates, helados) 🍦", "Salados o Ácidos (Papas, limón) 🍋"], index=None, label_visibility="collapsed")
    
    st.markdown("**2. ¿Cómo ha estado la energía?**")
    energia = st.radio("", ["Con mucho sueño 😴", "A tope de energía ⚡"], index=None, label_visibility="collapsed")
    
    st.write("  ")
    if st.button("ANALIZAR PISTAS 🧬"):
        if antojo and energia:
            avanzar_paso(3)
        else:
            st.warning("¡Responde las preguntas para continuar!")

# PASO 3: EL VOTO OFICIAL
elif st.session_state.paso == 3:
    st.markdown("<h1>📊 Análisis Completo</h1>", unsafe_allow_html=True)
    st.write("Las pistas son confusas... ¡La ciencia no puede decidir!")
    st.markdown("<h3>Es tu turno. Deja tu voto oficial:</h3>", unsafe_allow_html=True)
    st.write("  ")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='text-align:center; background-color:#e3f2fd; padding:15px; border-radius:20px;'><p style='font-size: 60px;'>🧸</p></div>", unsafe_allow_html=True)
        if st.button("💙 APUESTO POR NIÑO"):
            st.session_state.voto = "Niño"
            avanzar_paso(4)
    with col2:
        st.markdown("<div style='text-align:center; background-color:#fce4ec; padding:15px; border-radius:20px;'><p style='font-size: 60px;'>🎀</p></div>", unsafe_allow_html=True)
        if st.button("💖 APUESTO POR NIÑA"):
            st.session_state.voto = "Niña"
            avanzar_paso(4)

# PASO 4: EL CLIFFHANGER Y EL MAPA
elif st.session_state.paso == 4:
    st.markdown("<h1>¡Voto Registrado! ✅</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>Has apostado por {st.session_state.voto}... pero la verdad es que...</h3>", unsafe_allow_html=True)
    
    revelar = st.button("VER RESULTADO FINAL 🫣")

    if revelar:
        placeholder = st.empty()
        for i in range(3, 0, -1):
            placeholder.markdown(f"<h1 style='font-size: 100px; color: #9D50BB; text-align:center;'>{i}</h1>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()

        st.markdown("<p class='misterio-final'>¡SE REVELARÁ EN LA FIESTA! 🎉</p>", unsafe_allow_html=True)
        st.write("Tendrás que acompañarnos para descubrir si ganaste tu apuesta.")
        
        st.divider()

        # Datos y Mapa
        st.markdown("<h1>📍 Coordenadas de la Revelación</h1>", unsafe_allow_html=True)
        
        det_col1, det_col2 = st.columns(2)
        with det_col1:
            st.markdown("<p style='font-size: 30px;'>📅</p>", unsafe_allow_html=True)
            st.markdown("<p><b>Sábado 20 de Junio</b><br>17:00 Hrs</p>", unsafe_allow_html=True)
        with det_col2:
            st.markdown("<p style='font-size: 30px;'>🏠</p>", unsafe_allow_html=True)
            st.markdown("<p><b>Calle Pargua 8999</b><br>Cerrillos, Santiago</p>", unsafe_allow_html=True)

        st.divider()

        # Mapa de Cerrillos
        lat_fija = -33.501
        lon_fija = -70.710
        map_data = pd.DataFrame({'lat': [lat_fija], 'lon': [lon_fija]})
        st.map(map_data, zoom=14)

        direccion_query = "Pargua+8999+Cerrillos+Santiago"
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={direccion_query}"
        
        st.write("  ")
        st.link_button("🗺️ CÓMO LLEGAR (ABRIR EN MAPAS) 🗺️", google_maps_url)
