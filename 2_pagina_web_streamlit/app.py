import streamlit as st
import whisper
import tempfile
import os
import json

# Cargar el modelo de Whisper (una vez)
modelo = whisper.load_model("base")

# Título de la app
st.title("Transcriptor de Audio con Whisper")

# Instrucciones
st.markdown("""
Sube un archivo de audio en formato `.wav`, `.mp3` u otro compatible.
El modelo Whisper transcribirá el audio y mostrará el texto aquí.
""")

# Cargar archivo
archivo_audio = st.file_uploader("Sube tu archivo de audio", type=["wav", "mp3", "m4a"])

if archivo_audio is not None:
    # Guardar archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(archivo_audio.read())
        ruta_temporal = temp_audio.name

    st.success("Archivo cargado con éxito. Procesando...")

    # Procesar el audio
    with st.spinner("Transcribiendo..."):
        resultado = modelo.transcribe(ruta_temporal)
        texto = resultado["text"]
    
    # Mostrar resultado
    st.subheader("Texto transcrito:")
    st.write(texto)

    # Mostrar JSON completo (opcional)
    with st.expander("Ver resultado completo (JSON)"):
        st.json(resultado)

    # Eliminar el archivo temporal
    os.remove(ruta_temporal)
