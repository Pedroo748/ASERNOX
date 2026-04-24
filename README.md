import streamlit as st

import streamlit as st
import time
import pandas as pd

# 1. Configuración de página con estética minimalista
st.set_page_config(page_title="Nuestra Revelación Mágica", page_icon="💌", layout="centered")

# 2. CSS AVANZADO: Modelado de Control y Estilo "Card" (Cartas)
# Esto hará que la app se vea profesional, con sombras y bordes suaves.
st.markdown("""
    <style>
    /* Fondo general */
    .stApp { background-color: #f0f2f6; }
    
    /* Modelado del contenedor principal como una "Carta" */
    .block-container {
        background-color: #ffffff;
        padding: 40px !important;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-top: 50px;
    }

    /* Estilo de títulos elegantes */
    h1 { color: #2c3e50; text-align: center; font-family: 'Helvetica Neue', sans-serif; font-weight: 800; }
    h3 { color: #7f8c8d; text-align: center; font-weight: 400; }
    p { text-align: center; color: #7f8c8d; font-size: 1.1rem; }

    /* Botones Premium Dinámicos (Gradiente Rosa/Azul) */
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
        background: linear-gradient(135deg, #FFBBEC 0%, #A9C9FF 100%);
    }

    /* Estilo para el texto de revelación final */
    .revelacion-final {
        font-size: 60px !important;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(#FF99CC, #FFB6C1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Control de Estado (Navegación Dinámica)
if 'paso' not in st.session_state:
    st.session_state.paso = 1

def avanzar_paso(nuevo_paso):
    st.session_state.paso = nuevo_paso
    st.rerun()

# 4. Flujo de la Invitación DInámica
# -----------------------------------

# PASO 1: EL SOBRE MÁGICO (Animación inicial)
if st.session_state.paso == 1:
    st.markdown("<h1>✨ Ha llegado una carta especial ✨</h1>", unsafe_allow_html=True)
    # Usamos un emoji gigante como imagen dinámica
    st.markdown("<p style='font-size: 120px; text-align: center; margin-top: -30px;'>✉️</p>", unsafe_allow_html=True)
    st.markdown("<h3>Alguien muy pequeño tiene un mensaje enorme para ti...</h3>", unsafe_allow_html=True)
    st.write("  ") # Espaciador
    if st.button("ABRIR LA CARTA 💖"):
        avanzar_paso(2)

# PASO 2: LA APUESTA INTERACTIVA
elif st.session_state.paso == 2:
    st.markdown("<h1>🤔 ¿Qué crees que soy?</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Vota por tu Team favorito antes de la verdad:</h3>", unsafe_allow_html=True)
    st.write("  ") # Espaciador

    # Modelado de columnas para las "cartas" de voto
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='text-align:center; background-color:#e3f2fd; padding:20px; border-radius:20px;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 80px;'>🧸</p>", unsafe_allow_html=True)
        if st.button("💙 TEAM NIÑO"):
            st.session_state.voto = "un Niño 👦"
            avanzar_paso(3)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='text-align:center; background-color:#fce4ec; padding:20px; border-radius:20px;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 80px;'>🎀</p>", unsafe_allow_html=True)
        if st.button("💖 TEAM NIÑA"):
            st.session_state.voto = "una Niña 👧"
            avanzar_paso(3)
        st.markdown("</div>", unsafe_allow_html=True)

# PASO 3: LA REVELACIÓN Y EL MAPA (El clímax)
elif st.session_state.paso == 3:
    st.markdown(f"<h3>Tu corazón apostaba por {st.session_state.voto}</h3>", unsafe_allow_html=True)
    st.markdown("<h1>¡Prepárate para la sorpresa! 🎉</h1>", unsafe_allow_html=True)
    
    revelar = st.button("🎬 ¡INICIAR REVELACIÓN! 🎬")

    if revelar:
        placeholder = st.empty()
        # Cuenta regresiva dinámica con colores cambiantes
        for i in range(3, 0, -1):
            color = "#A9C9FF" if i % 2 != 0 else "#FFBBEC"
            placeholder.markdown(f"<h1 style='font-size: 120px; color: {color}; text-align:center;'>{i}</h1>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()

        # --- EFECTO FINAL POTENTE ---
        st.balloons() # Lanza globos
        st.snow()     # Agrega copos tierno (opcional)

        # RESULTADO (editable: NIÑA o NIÑO)
        st.markdown("<p class='revelacion-final'>¡ES UNA NIÑA! 🎀</p>", unsafe_allow_html=True)
        
        st.divider()

        # --- SECCIÓN DE DATOS Y MAPA INTERACTIVO DlNÁMICO ---
        st.markdown("<h1>📍 ¿Dónde y Cuándo?</h1>", unsafe_allow_html=True)
        st.divider()

        # Detalles en columnas
        det_col1, det_col2 = st.columns(2)
        with det_col1:
            st.markdown("<p style='font-size: 30px;'>📅</p>", unsafe_allow_html=True)
            st.markdown("<p><b>Sábado 20 de Junio</b><br>17:00 Hrs</p>", unsafe_allow_html=True)
        with det_col2:
            st.markdown("<p style='font-size: 30px;'>🏠</p>", unsafe_allow_html=True)
            st.markdown("<p><b>Calle Pargua 8999</b><br>Cerrillos, Santiago</p>", unsafe_allow_html=True)

        st.divider()

        # -- IMPLEMENTACIÓN DEL MAPA --
        # Coordenadas de ejemplo cerca de Pargua 8999, Cerrillos
        lat_fija = -33.501
        lon_fija = -70.710
        map_data = pd.DataFrame({'lat': [lat_fija], 'lon': [lon_fija]})

        # Mostramos el mapa centrado
        st.write("### Toca el mapa para ver la ubicación:")
        st.map(map_data, zoom=14)

        # -- BOTÓN DlNÁMICO PARA ABRIR EN GOOGLE MAPS/WAZE --
        # Como tocar el mapa integrado no abre la app externa directamente,
        # creamos un botón prominente justo debajo que hace exactamente eso.
        direccion_query = "Pargua+8999+Cerrillos+Santiago"
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={direccion_query}"
        
        st.write("  ") # Espaciador
        st.link_button("🗺️ CÓMO LLEGAR (ABRIR EN MAPAS/WAZE) 🗺️", google_maps_url)
        
        st.success("¡Te esperamos para celebrar juntos!")
