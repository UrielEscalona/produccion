import os
from flask import Flask, request, render_template, send_from_directory
from detector import detectar_objetos

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    imagen_resultado = None
    if request.method == "POST":
        archivo = request.files["imagen"]
        if archivo and archivo.filename != "":
            ruta = os.path.join(UPLOAD_FOLDER, archivo.filename)
            archivo.save(ruta)
            resultado, imagen_resultado = detectar_objetos(ruta)
    return render_template("index.html", resultado=resultado, imagen=imagen_resultado)

@app.route("/static/<filename>")
def imagen_procesada(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)