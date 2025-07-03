import os
import sys
import json
import logging
import whisper
from typing import Dict, Union


# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)  # Log a la consola
    ]
)
logger = logging.getLogger(__name__)

FORMATOS_SOPORTADOS = ('.wav', '.mp3', '.flac', '.ogg')


def procesar_audio(ruta_audio: str) -> Dict[str, Union[str, None]]:
    """
    Función para procesar un archivo de audio y transcribirlo a texto.

    Args:
        ruta_audio (str): Ruta al archivo de audio a procesar.
    Returns:
        dict: Un diccionario con la transcripción del audio.
    """

    if not os.path.exists(ruta_audio):
        raise FileNotFoundError(f"El archivo {ruta_audio} no existe.")
    
    if not os.access(ruta_audio, os.R_OK):
        raise PermissionError(f"No se puede leer el archivo {ruta_audio}.")

    if not ruta_audio.lower().endswith(FORMATOS_SOPORTADOS):
        raise ValueError(f"Formato no soportado. Use: {', '.join(FORMATOS_SOPORTADOS)}") 
    
    try:
        logger.info(f"Procesando archivo: {ruta_audio}")
        resultado = modelo.transcribe(ruta_audio)
        logger.debug("Transcripción completada con éxito")
        return {"texto": resultado["text"]}
    
    except Exception as e:
        logger.error(f"Error al procesar {ruta_audio}: {str(e)}", exc_info=True)
        return {"error": str(e)}

def main(ruta_audio: str) -> None:
    """
    Función principal que carga el modelo y procesa el archivo de audio.

    Args:
        ruta_audio (str): Ruta al archivo de audio a procesar.
    """
    
    resultado = procesar_audio(ruta_audio)

    logger.info(
        "Resultado:\n" + json.dumps(resultado, ensure_ascii=False, indent=2)
        )
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Uso: python script.py ruta/al/audio.[wav|mp3|flac|ogg]")
        sys.exit(1)
    
    logger.info("Cargando modelo Whisper...")
    modelo = whisper.load_model("base")
    logger.info("Modelo cargado correctamente")

    main(sys.argv[1])
    

