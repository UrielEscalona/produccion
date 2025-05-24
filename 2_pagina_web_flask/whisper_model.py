import whisper

# Cargar modelo una vez
modelo = whisper.load_model("base")

def procesar_audio(ruta_audio):
    resultado = modelo.transcribe(ruta_audio)
    return resultado["text"]
