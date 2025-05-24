from flask import Flask, render_template, request
from whisper_model import procesar_audio
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Asegúrate que la carpeta de uploads exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    transcripcion = None
    if request.method == "POST":
        if "archivo" not in request.files:
            return "No se subió ningún archivo"
        
        archivo = request.files["archivo"]
        if archivo.filename == "":
            return "Nombre de archivo vacío"

        ruta = os.path.join(app.config["UPLOAD_FOLDER"], archivo.filename)
        archivo.save(ruta)

        transcripcion = procesar_audio(ruta)
    
    return render_template("index.html", transcripcion=transcripcion)

if __name__ == "__main__":
    app.run(debug=True)
