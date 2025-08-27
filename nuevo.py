from estadisticas_zombies import zombies
import os

def obtener_ruta_ronda(numero_ronda):
    nombre_archivo = "ronda_" + numero_ronda + ".txt"
    ruta_carpeta = os.path.dirname(__file__)
    ruta_rondas = os.path.join(ruta_carpeta, "rondas")
    ruta_archivo = os.path.join(ruta_rondas, nombre_archivo)

    return ruta_archivo

def leer_ronda():
    ruta_archivo = obtener_ruta_ronda(numero_ronda = "1")
    with open(ruta_archivo, "r") as ronda:
        for subronda in ronda:
            obtener_datos_enemigos(subronda)

def obtener_datos_enemigos(subronda):
    zombies_presentes = subronda.split()
    for zombie in zombies_presentes:
        datos = zombies[zombie]
        vida = datos["vida"]
        velocidad = datos["velocidad"]
        daño = datos["daño"]
        recompensa = datos["recompensa"]