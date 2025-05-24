# 🌐 Interfaz Web para Whisper usando Docker

Este proyecto permite utilizar una interfaz web local para subir archivos de audio `.wav` y transcribirlos a texto usando el modelo **Whisper** de OpenAI. Todo el procesamiento se realiza ejecutando un contenedor Docker que contiene Whisper, desde un backend Flask simple.

---

## 📁 Estructura del proyecto

```
produccion/
├── 3_docker/               # Contenedor Docker con Whisper
│   ├── Dockerfile
│   ├── procesar_audio.py
│   ├── requirements.txt
│   └── audio/              # Aquí se copian los archivos subidos por la web
└── 3_docker_web/           # Web con Flask
    ├── app.py              # Backend Flask
    ├── templates/
    │   └── index.html      # Interfaz web
    └── audio/              # Audios subidos por el usuario
```

---

## ⚙️ Requisitos

- Python 3.10+ (con `flask` instalado)
- Docker (y tener funcionando el contenedor `whisper_app`)
- Sistema operativo que soporte ejecución de comandos Docker (Linux, macOS o Windows con WSL o Docker Desktop)

---

## 🚀 Instrucciones de uso

### 1️⃣ Construir el contenedor Whisper (si no lo has hecho)

```bash
cd 3_docker
docker build -t whisper_app .
```

### 2️⃣ Ejecutar el servidor Flask

```bash
cd 3_docker_web
pip install flask
python app.py
```

Esto iniciará un servidor en [http://localhost:5000](http://localhost:5000)

### 3️⃣ Usar la aplicación

- Abre el navegador
- Sube un archivo `.wav`
- Recibirás la transcripción directamente en pantalla

---

## 🧠 Cómo funciona

1. El usuario sube un archivo `.wav` a través del navegador.
2. Flask guarda el archivo en `3_docker_web/audio/`
3. Flask copia ese archivo a `3_docker/audio/`, donde el contenedor Docker puede accederlo.
4. Se ejecuta el contenedor Docker `whisper_app` con `docker run`, pasando el archivo como argumento.
5. La salida (transcripción) es capturada y mostrada en la página.

---

## ⚠️ Posibles errores comunes

| Error | Causa | Solución |
|------|-------|----------|
| `can't open file 'procesar_audio.py'` | El contenedor no encuentra el script | Asegúrate de montar `3_docker` como volumen correctamente |
| `No such file or directory: audio/audio.wav` | El archivo `.wav` no fue copiado a `3_docker/audio` | Flask ya lo copia automáticamente en esta versión |
| `UnicodeDecodeError` | Salida con caracteres UTF-8 mal decodificados | Se resuelve usando `encoding='utf-8'` en `subprocess.check_output()` |

---

## ✅ Ventajas de este sistema

- Permite utilizar Whisper sin interfaz de consola
- No necesitas conocimientos de Python para transcribir audios
- Ideal para pruebas locales, proyectos personales o demo en computadoras con Docker

---

Desarrollado por [Uriel Escalona](https://github.com/UrielEscalona)