from fastapi import FastAPI, Query, File, UploadFile
from pydantic import BaseModel
from PIL import Image
from io import BytesIO

app = FastAPI()

# Endpoint GET
@app.get("/mayusculas/")
def convertir_a_mayusculas(oracion: str = Query(..., description="Oración a convertir en mayúsculas")):
    return {"resultado": oracion.upper()}

# Endpoint POST con JSON
class Entrada(BaseModel):
    oracion: str

@app.post("/mayusculas/")
def convertir_post(data: Entrada):
    return {"resultado": data.oracion.upper()}

# Endpoint POST para imágenes
@app.post("/imagen/")
async def procesar_imagen(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    width, height = image.size
    return {
        "nombre_archivo": file.filename,
        "formato": image.format,
        "ancho": width,
        "alto": height
    }
