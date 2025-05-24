# 🐳 Transcriptor de Audio con Whisper y Docker

Este proyecto permite transcribir archivos de audio `.wav` utilizando el modelo Whisper de OpenAI, empaquetado en un contenedor Docker. Es ideal para quienes buscan una solución portable y reproducible sin instalar dependencias en su sistema local.

---

## 🔰 1. Introducción

El objetivo es crear una aplicación mínima que use el modelo Whisper para convertir voz en texto. Este sistema se ejecuta desde un contenedor Docker, garantizando compatibilidad y portabilidad.

---

## ⚙️ 2. Configuración Local Inicial (opcional)

Si deseas probar primero sin Docker, puedes crear un entorno virtual con Anaconda y verificar que Whisper funcione localmente:

### 2.1 Crear entorno con Anaconda

```bash
conda create -n whisper_env python=3.10 -y
conda activate whisper_env
```

### 2.2 Instalar dependencias

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 2.3 Verificar GPU

```python
import torch
print(torch.cuda.is_available())
```

---

## 🐳 3. Preparación para Docker

### 3.1 Estructura esperada

```
3_docker/
├── Dockerfile
├── requirements.txt
├── procesar_audio.py
└── audio.wav
```

### 3.2 Script de transcripción (`procesar_audio.py`)

Este archivo contiene el código para cargar el modelo y transcribir un archivo `.wav` recibido como argumento desde consola.

---

## 📦 4. Archivos Clave

### 4.1 `requirements.txt`

Contiene las dependencias necesarias para instalar Whisper, PyTorch con soporte CUDA, y una versión compatible de NumPy.

### 4.2 `Dockerfile`

Define la imagen base de Python, instala `ffmpeg`, copia el código y las dependencias, y define el comando por defecto.

---

## 🛠️ 5. Uso del contenedor

### 5.1 Construcción

```bash
docker build -t whisper_app .
```

### 5.2 Ejecución

```bash
docker run --rm -v %cd%:/app whisper_app python procesar_audio.py audio.wav
```

> En Linux/macOS usa `$(pwd)` en lugar de `%cd%`.

---

## ⚠️ 6. Posibles errores y soluciones

| Problema | Solución |
|---------|----------|
| `can't open file` | Asegúrate de que los archivos estén dentro de la carpeta montada y el Dockerfile tenga `COPY . .` |
| `Numpy is not available` | Usa `numpy<2.0` en `requirements.txt` |
| `torch` no se encuentra | Añade `--extra-index-url https://download.pytorch.org/whl/cu118` |
| `audio.wav` no encontrado | Usa correctamente el `-v` para montar el volumen con tu carpeta local |

---

## ▶️ 7. Automatización (opcional)

Crea un archivo `transcribir.bat` en Windows para facilitar su uso:

```bat
@echo off
docker run --rm -v %cd%:/app whisper_app python procesar_audio.py %1
```

Y luego simplemente ejecuta:

```bash
transcribir.bat audio.wav
```

---

## 🏁 8. Conclusión

- Entorno autocontenible, reproducible en cualquier máquina con Docker.
- Aislamiento de dependencias.
- Compatible con aceleración por GPU (si Docker está configurado para usarla).

---

Desarrollado por [Uriel Escalona](https://github.com/UrielEscalona)