import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
from PIL import Image

# Cargar modelo YOLOv8n
modelo = YOLO("yolov8n.pt")

# Configurar página
st.set_page_config(page_title="Detector de Objetos", page_icon="🔍", layout="centered")
st.title("🔍 Detector de Objetos con YOLOv8n")
st.markdown("Sube una imagen y detectaremos automáticamente los objetos presentes usando un modelo ligero de YOLO.")

# Subida de imagen
imagen_subida = st.file_uploader("📤 Sube tu imagen (formatos aceptados: JPG, PNG)", type=["jpg", "jpeg", "png"])

# Procesamiento
if imagen_subida is not None:
    st.markdown("---")
    imagen_pil = Image.open(imagen_subida).convert("RGB")
    st.image(imagen_pil, caption="📷 Imagen original", use_column_width=True)

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        imagen_pil.save(tmp.name)
        ruta_temporal = tmp.name

    resultados = modelo(ruta_temporal)[0]

    imagen_np = np.array(imagen_pil)
    for box in resultados.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        clase = resultados.names[int(box.cls[0])]
        label = f"{clase} ({conf:.0%})"
        cv2.rectangle(imagen_np, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(imagen_np, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    st.image(imagen_np, caption="🧠 Resultado de la detección", use_column_width=True)

    st.markdown("### 🔎 Objetos detectados:")
    for box in resultados.boxes:
        clase = resultados.names[int(box.cls[0])]
        conf = box.conf[0].item()
        st.success(f"✔️ {clase}: {conf:.1%}")