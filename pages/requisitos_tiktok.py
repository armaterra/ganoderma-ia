import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Requisitos para TikTok Developers",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Requisitos para Desarrolladores de TikTok")
st.markdown("Esta página contiene la información necesaria para registrar tu aplicación en el portal de desarrolladores de TikTok.")

# --- Descripción de la app (máx 120 caracteres) ---
st.subheader("📝 Descripción de la Aplicación")
st.write("""
**GUATEVITA** es una plataforma que permite a distribuidores independientes de productos PIOIR publicar contenido motivacional y gestionar mensajes directos con clientes potenciales en TikTok.
""")
# Conteo de caracteres
desc = "GUATEVITA es una plataforma que permite a distribuidores independientes de productos PIOIR publicar contenido motivacional y gestionar mensajes directos con clientes potenciales en TikTok."
st.caption(f"Caracteres: {len(desc)} / 120")

st.divider()

# --- Términos de Servicio ---
st.subheader("📜 Términos de Servicio")
st.markdown("""
**Fecha de última actualización:** 18 de agosto de 2026

**1. Aceptación de los Términos**  
Al utilizar esta aplicación y el sitio web `www.imaa.digital`, usted acepta estos Términos de Servicio. Si no está de acuerdo, no utilice la aplicación.

**2. Descripción del Servicio**  
La aplicación GUATEVITA permite a los distribuidores independientes de productos PIOIR publicar contenido motivacional y gestionar interacciones con clientes potenciales a través de mensajes directos en TikTok. La aplicación no vende productos directamente, sino que facilita la comunicación y la difusión de información sobre el estilo de vida y la oportunidad de negocio.

**3. Responsabilidades del Usuario**  
- El usuario se compromete a utilizar la aplicación únicamente para fines lícitos y de acuerdo con las políticas de Gano Excel.  
- No se permite el uso de la aplicación para difundir información falsa, engañosa o que infrinja derechos de propiedad intelectual.  
- El usuario es responsable de las publicaciones y mensajes enviados a través de la aplicación.

**4. Propiedad Intelectual**  
La aplicación y su contenido (textos, diseños, logotipos) son propiedad de GUATEVITA o de sus licenciantes. El usuario no adquiere ningún derecho de propiedad sobre el contenido generado por la aplicación.

**5. Limitación de Responsabilidad**  
La aplicación se proporciona "tal cual". GUATEVITA no garantiza que la aplicación esté libre de errores o que el acceso sea ininterrumpido. En ningún caso GUATEVITA será responsable por daños indirectos, incidentales o consecuentes derivados del uso de la aplicación.

**6. Modificaciones**  
GUATEVITA se reserva el derecho de modificar estos términos en cualquier momento. Las modificaciones serán efectivas al ser publicadas en esta página.
""")

st.divider()

# --- Política de Privacidad ---
st.subheader("🔒 Política de Privacidad")
st.markdown("""
**Fecha de última actualización:** 18 de agosto de 2026

**1. Información que Recopilamos**  
Recopilamos la siguiente información cuando usted utiliza nuestra aplicación:  
- Nombre y apellidos.  
- Número de teléfono y/o identificador de TikTok.  
- Mensajes e interacciones a través de la aplicación.  
- Datos de uso (frecuencia de acceso, páginas visitadas).

**2. Uso de la Información**  
Utilizamos la información para:  
- Proporcionar y mejorar nuestros servicios.  
- Responder a sus consultas y gestionar su cuenta de distribuidor.  
- Enviarle información sobre promociones o novedades (si ha dado su consentimiento).  
- Cumplir con obligaciones legales.

**3. Almacenamiento y Seguridad**  
Sus datos se almacenan en servidores seguros en la nube. Implementamos medidas de seguridad técnicas y organizativas para proteger su información contra accesos no autorizados.

**4. Compartición de Datos**  
No compartimos sus datos personales con terceros, excepto cuando sea necesario para cumplir con la ley o para proveer servicios (ej. proveedores de hosting, pasarelas de pago). Todos nuestros proveedores están sujetos a cláusulas de confidencialidad.

**5. Sus Derechos**  
Usted tiene derecho a acceder, rectificar, cancelar u oponerse al tratamiento de sus datos personales. Para ejercer estos derechos, puede contactarnos a través de los canales indicados en nuestro sitio web.

**6. Cookies**  
Nuestro sitio utiliza cookies para mejorar la experiencia de usuario y analizar el tráfico. Puede configurar su navegador para rechazar las cookies, aunque esto podría afectar la funcionalidad del sitio.
""")

st.divider()

# --- Enlaces (simulados) ---
st.subheader("🔗 Enlaces para TikTok")
st.write("""
- **Términos de Servicio:** `https://www.imaa.digital/terms`  
- **Política de Privacidad:** `https://www.imaa.digital/privacy`  
- **URL de la aplicación:** `https://www.imaa.digital/app`
""")
st.caption("Estos enlaces son referenciales; en producción deben apuntar a las páginas reales.")
