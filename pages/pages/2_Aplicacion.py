import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="GUATEVITA - Aplicación",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .landing-title { font-size: 3.5rem; font-weight: 700; color: #1A3A5C; }
    .landing-sub { font-size: 1.8rem; color: #4A6A8C; }
    .feature-box { background-color: #F8FAFC; padding: 1.5rem; border-radius: 12px; margin: 1rem 0; }
    .cta-button { background-color: #2E4057; color: white; padding: 0.8rem 2rem; border-radius: 8px; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# --- Encabezado con imagen ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<p class="landing-title">☕ GUATEVITA</p>', unsafe_allow_html=True)
    st.markdown('<p class="landing-sub">Tu Camino hacia el Bienestar</p>', unsafe_allow_html=True)
with col2:
    st.image(
        "https://private-user-images.githubusercontent.com/304722560/637807346-ebfa9f72-ee01-4ef8-a55e-c0b7c7a9d1e6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODcwODYxNzYsIm5iZiI6MTc4NzA4NTg3NiwicGF0aCI6Ii8zMDQ3MjI1NjAvNjM3ODA3MzQ2LWViZmE5ZjcyLWVlMDEtNGVmOC1hNTVlLWMwYjdjN2E5ZDFlNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwODE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDgxOFQyMDQ0MzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTFlNTM1N2EzZjc2ZjdhNDkyZTMxMjdmNzhlYTQzNmEyNjc3MWRmZDhiNGJhYTJmOTJmYWZkZjNhN2ZiMTMzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.5QEjSUEU5-r7OCqx14Yy1bLem-Oei2BDbmSMGEvP9kQ",
        use_column_width=True
    )

st.divider()

# --- Visión Integral del Negocio ---
st.markdown("## 🌟 Visión Integral")
st.write("""
**GUATEVITA** es más que un café; es un movimiento hacia un estilo de vida más saludable y emprendedor. 

Nuestro propósito es ofrecer a las personas la oportunidad de mejorar su bienestar a través de productos funcionales de alta calidad, mientras construyen una fuente de ingresos complementaria mediante una red de distribución.

**¿Qué ofrecemos?**
- **Productos de vanguardia:** Bebidas y suplementos enriquecidos con Ganoderma lucidum, respaldados por más de 30 años de investigación.
- **Un modelo de negocio probado:** Basado en el consumo, la recomendación y la invitación, con un plan de compensación de 12 formas de ganar.
- **Formación y acompañamiento:** Herramientas, asesoría y una comunidad global que te apoya en cada paso.

**¿Cómo funciona?**
1. Te conviertes en distribuidor independiente adquiriendo un Paquete Empresarial.
2. Disfrutas los productos, los compartes con tu círculo y construyes tu red.
3. Obtienes ingresos por tus ventas y por el volumen de tu equipo, generando un flujo residual a largo plazo.
""")

# --- Características destacadas ---
st.markdown("## 🚀 Características Clave")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-box">
        <h4>✅ Producto Premium</h4>
        <p>Café y chocolate con extracto de Ganoderma, sin conservantes artificiales.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-box">
        <h4>💰 Modelo Rentable</h4>
        <p>Comisiones por ventas directas, reclutamiento y volumen de red.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-box">
        <h4>🌐 Comunidad Global</h4>
        <p>Presencia en más de 70 países y una red de líderes que te guían.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Llamado a la acción ---
st.markdown("## 📲 Conéctate con nosotros")
st.write("""
¿Listo para empezar tu viaje hacia el bienestar y la libertad financiera? 
Síguenos en TikTok y envíanos un mensaje directo para recibir más información o comenzar tu proceso de afiliación.
""")
st.markdown("""
<a href="https://www.tiktok.com/@guatevita" target="_blank" style="background-color:#2E4057; color:white; padding:0.8rem 2rem; border-radius:8px; text-decoration:none; display:inline-block;">
    📱 Visítanos en TikTok
</a>
""", unsafe_allow_html=True)

st.divider()
st.caption("© 2026 GUATEVITA – Distribuidor Independiente de Gano Excel")
