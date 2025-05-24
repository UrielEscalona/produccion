# 🌐 Nivel 2: Aplicación Web con Flask

Esta carpeta contiene una aplicación web sencilla construida con Flask que permite a los usuarios subir archivos de audio y obtener su transcripción utilizando el modelo Whisper de OpenAI.

---

## 📁 Estructura del Proyecto

```
2_pagina_web_flask/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── uploads/
├── transcripciones/
├── requirements.txt
└── README.md
```

- `app.py`: Archivo principal que contiene la lógica de la aplicación Flask.
- `templates/index.html`: Plantilla HTML para la interfaz de usuario.
- `static/styles.css`: Archivo CSS para estilos personalizados.
- `uploads/`: Carpeta donde se almacenan temporalmente los archivos de audio subidos.
- `transcripciones/`: Carpeta donde se guardan las transcripciones generadas.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar la aplicación.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- [Anaconda](https://www.anaconda.com/) (opcional pero recomendado)
- Dependencias listadas en `requirements.txt`

---

## 🛠️ Instalación y Ejecución

1. **Clonar el repositorio o descargar esta carpeta:**

   ```bash
   git clone https://github.com/tu_usuario/produccion.git
   cd produccion/2_pagina_web_flask
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

   ```bash
   conda create -n flask_env python=3.10
   conda activate flask_env
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**

   ```bash
   python app.py
   ```

5. **Acceder a la aplicación:**

   Abre tu navegador y ve a `http://127.0.0.1:5000/`

---

## 🚀 Uso de la Aplicación

1. En la página principal, haz clic en "Seleccionar archivo" y elige un archivo de audio en formato `.wav`.
2. Haz clic en "Subir y Transcribir".
3. La aplicación procesará el audio y mostrará la transcripción en pantalla.
4. La transcripción también se guardará en la carpeta `transcripciones/`.

---

## 🧠 Notas

- Esta aplicación utiliza el modelo `base` de Whisper de OpenAI para la transcripción de audio.
- Asegúrate de que los archivos de audio estén en formato `.wav` y sean de buena calidad para obtener mejores resultados.
- Esta es una implementación básica destinada a propósitos educativos y puede ser mejorada para uso en producción.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Siéntete libre de usarlo y adaptarlo según tus necesidades.

---

## ✨ Créditos

Desarrollado por [Uriel Escalona](https://github.com/UrielEscalona). Este proyecto forma parte de una serie de ejemplos para aprender a poner modelos de IA en producción.
