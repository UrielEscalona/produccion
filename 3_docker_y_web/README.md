# 🐳 Interfaz Web Embebida con Whisper (CPU + Flask en un solo contenedor)

Este proyecto contiene una aplicación **totalmente autocontenida** para transcribir archivos `.wav` usando el modelo **Whisper de OpenAI**. La interfaz web y el procesamiento están integrados en un solo contenedor Docker, funcionando en CPU (no requiere GPU).

---

## 🌐 ¿Qué hace esta aplicación?

- Ejecuta un **servidor web Flask**
- Permite **subir archivos de audio `.wav`** desde el navegador
- Usa **Whisper en modo CPU** para transcribir el audio
- Devuelve la transcripción en la misma página web

Todo esto desde un único contenedor Docker, accesible en:

📍 **http://127.0.0.1:5000/**

---

## 🧱 Estructura del proyecto

```
3_docker_y_web/
├── Dockerfile              # Contenedor único: Flask + Whisper
├── requirements.txt        # Dependencias para CPU
├── app.py                  # Lógica web y de transcripción
├── procesar_audio.py       # Script que usa Whisper
├── templates/
│   └── index.html          # Interfaz web HTML
├── static/                 # Archivos estáticos (vacío)
└── audio/                  # Carpeta temporal para subir .wav
```

---

## ⚙️ Requisitos

- Tener instalado **Docker Desktop** (Windows/macOS/Linux)
- Acceso a navegador web

No se necesita instalar Python localmente ni Whisper manualmente.

---

## 🚀 Instrucciones de uso

### 1️⃣ Construir la imagen

```bash
docker build -t whisper_web_cpu .
```

### 2️⃣ Ejecutar el contenedor

```bash
docker run --rm -p 5000:5000 whisper_web_cpu
```

### 3️⃣ Usar desde navegador

Abre [http://127.0.0.1:5000/](http://127.0.0.1:5000/) y:

1. Sube un archivo `.wav`
2. Presiona "Transcribir"
3. Verás la transcripción en la misma página

---

## 🧠 ¿Cómo funciona internamente?

- El usuario sube un archivo `.wav`
- Flask lo guarda en la carpeta `/app/audio`
- Se llama localmente al script `procesar_audio.py`
- Este usa Whisper (`base` model en CPU) y devuelve la transcripción
- Flask muestra el resultado en la web

---

## ⚠️ Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `RuntimeError: Failed to load audio` | El archivo no se pudo procesar con ffmpeg | Asegúrate que es `.wav` válido |
| `torch` demasiado lento | Estás usando CPU | Esto es normal sin GPU |
| El sitio no carga | El contenedor no está corriendo | Revisa el comando `docker run` |

---

## 🏁 Conclusión

✅ Solución fácil, sin dependencias externas  
✅ Ideal para demos, entornos controlados o usuarios sin experiencia técnica  
✅ Portátil y lista para usar en cualquier sistema con Docker

---

Desarrollado por [Uriel Escalona](https://github.com/UrielEscalona)