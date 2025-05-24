import os
import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = "audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        archivo = request.files["audio"]
        if archivo and archivo.filename.endswith(".wav"):
            # Guardar en carpeta local de la web
            ruta_audio_web = os.path.join(UPLOAD_FOLDER, archivo.filename)
            archivo.save(ruta_audio_web)

            # Copiar a carpeta de 3_docker/audio para que el contenedor lo vea
            ruta_3docker = os.path.abspath("../3_docker/audio")
            os.makedirs(ruta_3docker, exist_ok=True)
            ruta_destino = os.path.join(ruta_3docker, archivo.filename)
            with open(ruta_audio_web, "rb") as src, open(ruta_destino, "wb") as dst:
                dst.write(src.read())

            try:
                comando = [
                    "docker", "run", "--rm",
                    "-v", f"{os.path.abspath('../3_docker')}:/app",
                    "whisper_app",
                    "python", "procesar_audio.py",
                    f"audio/{archivo.filename}"
                ]
                salida = subprocess.check_output(comando, stderr=subprocess.STDOUT, encoding="utf-8")
                resultado = salida
            except subprocess.CalledProcessError as e:
                resultado = f"Error:\n{e.output}"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
