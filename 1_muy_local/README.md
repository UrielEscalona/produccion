# 🎙️ Nivel 1: Muy Local - Transcripción de Audio con Whisper

Esta carpeta contiene un único archivo de Python que permite transcribir archivos de audio a texto utilizando el modelo Whisper de OpenAI.

---

## 📁 Estructura

```
1_muy_local/
└── whisperu.py
```

---

## ⚙️ Requisitos

Para ejecutar este ejemplo necesitas:

- Tener instalado [Anaconda](https://www.anaconda.com/)
- Crear un entorno y activarlo:
  ```bash
  conda create -n whisper_env python=3.10
  conda activate whisper_env
  ```
- Instalar Whisper con pip:
  ```bash
  pip install git+https://github.com/openai/whisper.git
  ```

---

## ▶️ Uso

Este script solo puede ejecutarse desde la **consola**. El comando es:

```bash
python whisperu.py ruta/al/audio.wav
```

Por ejemplo:

```bash
python whisperu.py ejemplo_audio.wav
```

El resultado se imprimirá en formato JSON directamente en la terminal, con el texto transcrito.

---

## ℹ️ Nota

Este ejemplo representa la **forma más básica de uso de un modelo de IA en producción**. No tiene interfaz gráfica ni despliegue en la web, pero es una excelente base para comprender cómo se puede usar localmente un modelo como Whisper.
