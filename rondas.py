from oleadas import procesar_oleada
from zombies import bleh

import os

def obtener_ruta_ronda(numero_ronda):
    nombre_archivo = "ronda_" + numero_ronda + ".txt"
    ruta_carpeta = os.path.dirname(__file__)
    ruta_rondas = os.path.join(ruta_carpeta, "rondas")
    ruta_archivo = os.path.join(ruta_rondas, nombre_archivo)
    return ruta_archivo

def procesar_ronda():
    ruta_archivo = obtener_ruta_ronda(numero_ronda = "1")
    with open(ruta_archivo, "r") as ronda:
        for oleada in ronda:
            bleh(oleada)