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
            ruta = os.path.join(UPLOAD_FOLDER, archivo.filename)
            archivo.save(ruta)
            try:
                salida = subprocess.check_output(
                    ["python", "procesar_audio.py", ruta],
                    stderr=subprocess.STDOUT,
                    encoding="utf-8"
                )
                resultado = salida
            except subprocess.CalledProcessError as e:
                resultado = f"Error:\n{e.output}"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)