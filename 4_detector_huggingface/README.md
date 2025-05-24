---
title: YOLOv8n Object Detector
emoji: 🧠
colorFrom: indigo
colorTo: green
sdk: streamlit
app_file: app.py
pinned: false
---

# 🧠 Detector de Objetos con YOLOv8n (Streamlit + Hugging Face)

Esta app permite subir imágenes y detectar objetos usando YOLOv8n, todo desde una interfaz web sencilla con Streamlit.

## 🚀 ¿Cómo usarlo en Hugging Face Spaces?

1. Sube esta carpeta como repositorio a Hugging Face.
2. Crea un nuevo Space de tipo **Streamlit**.
3. Asegúrate de que el archivo `yolov8n.pt` se descargue automáticamente o inclúyelo.

## 🛠️ Requisitos especiales

El archivo `yolov8n.pt` puede descargarse automáticamente así:

```python
from ultralytics import YOLO
YOLO('yolov8n.pt')
```

O puedes subirlo directamente en la raíz del repositorio.

## 💡 Créditos

Desarrollado por [Uriel Escalona](https://github.com/UrielEscalona)