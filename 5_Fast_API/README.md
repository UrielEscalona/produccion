# 🚀 Proyecto de API con FastAPI

Este repositorio contiene una API construida con **FastAPI**, que incluye múltiples funcionalidades para procesar texto e imágenes.

## 📦 Requisitos

- Python 3.7 o superior
- `pip` (gestor de paquetes de Python)

## ⚙️ Instalación

```bash
pip install fastapi[all] pillow
```

## 📁 Estructura del Proyecto

```
.
├── main_2.py          # Contiene todos los endpoints
└── README.md          # Instrucciones del proyecto
```

## ▶️ Ejecución

```bash
uvicorn main_2:app --reload
```

## 📘 Endpoints disponibles

### 🔤 1. Convertir texto a mayúsculas

#### GET `/mayusculas/?oracion=hola mundo`

**Parámetros:**  
- `oracion` (str): texto a convertir

**Respuesta:**
```json
{ "resultado": "HOLA MUNDO" }
```

#### POST `/mayusculas/`

**JSON de entrada:**
```json
{ "oracion": "buenos días" }
```

**Respuesta:**
```json
{ "resultado": "BUENOS DÍAS" }
```

---

### 🖼️ 2. Procesar imagen

#### POST `/imagen/`

Sube una imagen como archivo.

**Respuesta:**
```json
{
  "nombre_archivo": "foto.jpg",
  "formato": "JPEG",
  "ancho": 1280,
  "alto": 720
}
```

Puedes probarlo fácilmente en Swagger UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
