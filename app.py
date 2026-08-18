import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="GUATEVITA - Bienestar y Oportunidad",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilos personalizados (opcional) ---
st.markdown("""
<style>
    .main-header { font-size: 3rem; font-weight: 700; color: #2E4057; }
    .sub-header { font-size: 1.5rem; font-weight: 400; color: #6B7B8D; }
    .section-title { font-size: 2rem; font-weight: 600; color: #2E4057; margin-top: 2rem; }
    .product-image { border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .faq-question { font-weight: 600; color: #1A3A5C; margin-top: 1.2rem; }
    .faq-answer { margin-left: 1rem; color: #333; }
    .footer { margin-top: 3rem; padding: 1.5rem; background-color: #F0F4F8; border-radius: 8px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- Encabezado ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<p class="main-header">☕ GUATEVITA</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Bienestar y oportunidad, en cada taza</p>', unsafe_allow_html=True)
with col2:
    # Imagen del producto (URL proporcionada)
    st.image(
        "https://private-user-images.githubusercontent.com/304722560/637807346-ebfa9f72-ee01-4ef8-a55e-c0b7c7a9d1e6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODcwODYxNzYsIm5iZiI6MTc4NzA4NTg3NiwicGF0aCI6Ii8zMDQ3MjI1NjAvNjM3ODA3MzQ2LWViZmE5ZjcyLWVlMDEtNGVmOC1hNTVlLWMwYjdjN2E5ZDFlNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwODE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDgxOFQyMDQ0MzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTFlNTM1N2EzZjc2ZjdhNDkyZTMxMjdmNzhlYTQzNmEyNjc3MWRmZDhiNGJhYTJmOTJmYWZkZjNhN2ZiMTMzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.5QEjSUEU5-r7OCqx14Yy1bLem-Oei2BDbmSMGEvP9kQ",
        caption="PIOIR Café – Energía y Bienestar",
        use_column_width=True,
        output_format="png"
    )

st.divider()

# --- Sección: Nuestro Producto ---
st.markdown('<p class="section-title">🌟 Nuestro Producto</p>', unsafe_allow_html=True)
st.write("""
PIOIR Café es una bebida instantánea que combina café gourmet de alta calidad con extracto de **Ganoderma lucidum**, un hongo adaptógeno reconocido en la tradición asiática por sus propiedades para el bienestar general. 
Este producto no reemplaza ningún medicamento; es un **complemento alimenticio** que aporta energía y vitalidad, ideal para quienes buscan un estilo de vida activo y equilibrado.
""")

# --- Sección: Modelo de Negocio ---
st.markdown('<p class="section-title">📈 Modelo de Negocio</p>', unsafe_allow_html=True)
st.write("""
Nuestro modelo se basa en el **consumo, la recomendación y la invitación**. 
1. **Consume** el producto y conviértete en un experto.
2. **Recomiéndalo** a tu círculo de confianza, compartiendo tu experiencia.
3. **Invita** a las personas interesadas a unirse a tu red de distribución.

Como distribuidor independiente, generas ingresos por:
- **Ventas directas** a clientes.
- **Bonos por reclutamiento** (GEN5) al incorporar nuevos distribuidores.
- **Comisiones por volumen de red** (binario y liderazgo) basadas en el rendimiento de tu equipo.

La inversión inicial se realiza mediante un **Paquete Empresarial (ESP)**, que incluye productos y material publicitario. El ESP-1 tiene un costo aproximado de **$195 USD**.
""")

# --- Sección: Preguntas Frecuentes (FAQ) ---
st.markdown('<p class="section-title">❓ Preguntas Frecuentes</p>', unsafe_allow_html=True)

faqs = [
    {
        "p": "¿Qué es el Ganoderma lucidum?",
        "r": "Es un hongo adaptógeno con más de 200 nutrientes esenciales y antioxidantes. Tradicionalmente se ha utilizado para fortalecer el sistema inmunológico y mejorar la respuesta al estrés."
    },
    {
        "p": "¿Cómo puedo comenzar como distribuidor?",
        "r": "Debes adquirir un Paquete Empresarial (ESP) a través de tu patrocinador. Luego, recibirás acceso a una oficina virtual con herramientas de capacitación y seguimiento."
    },
    {
        "p": "¿Cuáles son los requisitos de actividad mensual?",
        "r": "Para mantener tu estatus y ser elegible a comisiones, debes acumular al menos **50 PV (Volumen Personal)** cada mes, lo que equivale a unas pocas cajas de producto."
    },
    {
        "p": "¿Puedo usar el logo de PIOIR en mis redes sociales?",
        "r": "El uso de la marca está restringido a materiales autorizados. Como distribuidor independiente, debes identificarte claramente como tal y no puedes presentarte como representante oficial de Gano Excel."
    },
    {
        "p": "¿Qué soporte recibo como distribuidor?",
        "r": "Dispones de una asesoría virtual con materiales de formación, webinars, y herramientas para la gestión de tu red. También puedes participar en eventos y capacitaciones presenciales."
    }
]

for item in faqs:
    st.markdown(f'<p class="faq-question">{item["p"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="faq-answer">{item["r"]}</p>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>© 2026 GUATEVITA – Distribuidor Independiente de Gano Excel</p>
    <p>Este sitio es operado por un distribuidor independiente. Los productos no curan enfermedades.</p>
    <p>Conéctate con nosotros: <a href="https://www.tiktok.com/@guatevita" target="_blank">@guatevita</a></p>
</div>
""", unsafe_allow_html=True)
