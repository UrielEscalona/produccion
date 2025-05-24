# 🌐 Nivel 2: Aplicación Web con Streamlit

Esta carpeta contiene una aplicación web construida con Streamlit que permite a los usuarios subir archivos de audio y obtener su transcripción utilizando el modelo Whisper de OpenAI.

---

## 📁 Estructura del Proyecto

```
2_pagina_web_streamlit/
├── app.py
├── requirements.txt
└── README.md
```

- `app.py`: Archivo principal que contiene la lógica de la aplicación Streamlit.
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
   git clone https://github.com/UrielEscalona/produccion.git
   cd produccion/2_pagina_web_streamlit
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

   ```bash
   conda create -n streamlit_env python=3.10
   conda activate streamlit_env
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**

   ```bash
   streamlit run app.py
   ```

5. **Acceder a la aplicación:**

   Abre tu navegador y ve a `http://localhost:8501/`

---

## 🚀 Uso de la Aplicación

1. En la página principal, haz clic en "Browse files" y elige un archivo de audio en formato `.wav`.
2. La aplicación procesará el audio y mostrará la transcripción en pantalla.

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
