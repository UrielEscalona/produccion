import sys
import json
import whisper

# Cargar modelo (solo una vez)
modelo = whisper.load_model("base")

def procesar_audio(ruta_audio):
    resultado = modelo.transcribe(ruta_audio)
    return {"texto": resultado["text"]}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python procesador_audio.py ruta/al/audio.wav")
        sys.exit(1)
    
    ruta_audio = sys.argv[1]
    resultado = procesar_audio(ruta_audio)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
