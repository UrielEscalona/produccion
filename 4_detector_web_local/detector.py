from ultralytics import YOLO
import cv2
import os

modelo = YOLO('yolov8n.pt')  # Asegúrate de que este archivo esté en el proyecto o descargado

def detectar_objetos(ruta_imagen):
    nombre_salida = "resultado.jpg"
    ruta_salida = os.path.join("static", nombre_salida)

    resultados = modelo(ruta_imagen)[0]

    imagen = cv2.imread(ruta_imagen)
    for box in resultados.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        clase = resultados.names[int(box.cls[0])]
        label = f"{clase}: {conf:.1%}"
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(imagen, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imwrite(ruta_salida, imagen)

    resumen = [f"{resultados.names[int(box.cls[0])]}: {box.conf[0].item():.1%}" for box in resultados.boxes]
    return resumen, nombre_salida