import json
import os

RUTA_ARCHIVO = os.path.join("data", "citas.json")


def cargar_citas() -> list:
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_citas(citas: list):
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)
