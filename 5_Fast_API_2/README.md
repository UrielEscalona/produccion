# 🧠 Detección de Objetos con FastAPI + YOLOv8n

Este proyecto utiliza **FastAPI** junto con **YOLOv8n** (modelo ligero de detección de objetos) para:

- Detectar objetos en imágenes
- Dibujar las cajas sobre las imágenes
- Descargar la imagen procesada

## 📦 Requisitos

Antes de ejecutar la API, instala las dependencias necesarias:

```bash
pip install fastapi[all] pillow opencv-python ultralytics
```

## ▶️ Ejecución

Inicia el servidor con:

```bash
uvicorn main:app --reload
```

Abre tu navegador en:

```
http://127.0.0.1:8000/docs
```

Desde ahí podrás probar todos los endpoints fácilmente con Swagger UI.

## 📘 Endpoints disponibles

### 1. `POST /detectar/`

Detecta objetos y devuelve un JSON con:

```json
{
  "archivo": "ejemplo.jpg",
  "detecciones": [
    {
      "clase": "person",
      "confianza": 0.95,
      "coordenadas": [x1, y1, x2, y2]
    },
    ...
  ]
}
```

### 2. `POST /detectar/imagen/`

Devuelve la **imagen procesada** (en formato PNG) con las cajas dibujadas.  
Útil para previsualizar directamente en navegador o herramientas como Postman.

### 3. `POST /detectar/descargar/`

Devuelve la imagen con detecciones pero con cabecera `Content-Disposition`, por lo que el navegador **forzará su descarga** como:

```
resultado_nombreoriginal.png
```

## 📁 Archivos

```
.
├── main.py        # Código de la API con FastAPI + YOLOv8n
└── README.md      # Instrucciones de uso
```

---

## 🧠 Autor

Este proyecto fue desarrollado por Uriel Escalona con fines educativos y demostrativos.

