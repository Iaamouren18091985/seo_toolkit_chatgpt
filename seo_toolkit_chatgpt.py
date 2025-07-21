
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Generador SEO con ChatGPT", layout="wide")
st.title("🧠 Herramienta SEO con IA (GPT-3.5)")

# Campo para la API Key
api_key = st.text_input("🔑 Ingresa tu OpenAI API Key", type="password")

# Campo para palabra clave
keyword = st.text_input("📌 Escribe tu palabra clave SEO:")

# Acción al presionar botón
if st.button("Generar artículo"):
    if not api_key:
        st.warning("⚠️ Por favor, ingresa tu API Key.")
    elif not keyword:
        st.warning("⚠️ Debes escribir una palabra clave.")
    else:
        with st.spinner("✍️ Generando artículo con ChatGPT..."):
            try:
                client = OpenAI(api_key=api_key)
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un redactor profesional experto en SEO."},
                        {"role": "user", "content": f"Escribe un artículo optimizado para SEO sobre '{keyword}' con títulos, subtítulos, introducción y conclusión. Usa un lenguaje claro y profesional."}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                contenido = respuesta.choices[0].message.content
                st.success("✅ Artículo generado con éxito.")
                st.subheader("📝 Contenido generado:")
                st.text_area("Resultado", value=contenido, height=400)
            except Exception as e:
                st.error(f"❌ Error: {e}")
