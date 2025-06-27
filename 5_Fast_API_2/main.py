from fastapi import FastAPI, File, UploadFile, Response
from io import BytesIO
from PIL import Image, ImageDraw
import cv2
import numpy as np
from ultralytics import YOLO

app = FastAPI()

# Cargar modelo YOLO ligero (yolov8n)
model = YOLO("yolov8n.pt")

# Endpoint básico: solo devuelve JSON de detecciones
@app.post("/detectar/")
async def detectar_imagen(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    img_array = np.array(image)
    results = model.predict(img_array)

    detecciones = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            bbox = box.xyxy[0].tolist()
            detecciones.append({
                "clase": label,
                "confianza": round(conf, 3),
                "coordenadas": bbox
            })

    return {
        "archivo": file.filename,
        "detecciones": detecciones
    }

# Endpoint que devuelve la imagen con las cajas dibujadas
@app.post("/detectar/imagen/")
async def detectar_imagen_con_cajas(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    img_array = np.array(image)
    results = model.predict(img_array)

    draw = ImageDraw.Draw(image)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            bbox = box.xyxy[0].tolist()
            draw.rectangle(bbox, outline="red", width=2)
            draw.text((bbox[0], bbox[1]), label, fill="white")

    # Convertir a bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format="PNG")
    return Response(content=img_bytes.getvalue(), media_type="image/png")

# Endpoint que permite descargar la imagen procesada
@app.post("/detectar/descargar/")
async def detectar_y_descargar(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    img_array = np.array(image)
    results = model.predict(img_array)

    draw = ImageDraw.Draw(image)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            bbox = box.xyxy[0].tolist()
            draw.rectangle(bbox, outline="red", width=2)
            draw.text((bbox[0], bbox[1]), label, fill="white")

    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return Response(
        content=output.read(),
        media_type="image/png",
        headers={"Content-Disposition": f"attachment; filename=resultado_{file.filename}"}
    )
