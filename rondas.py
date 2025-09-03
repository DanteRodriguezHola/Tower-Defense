from config import ventana, world, enemigos
from zombies import Enemy

import pygame as pg
import os

def obtener_ruta_ronda(numero_ronda):
    nombre_archivo = "ronda_" + numero_ronda + ".txt"
    ruta_carpeta = os.path.dirname(__file__)
    ruta_rondas = os.path.join(ruta_carpeta, "rondas")
    ruta_archivo = os.path.join(ruta_rondas, nombre_archivo)
    return ruta_archivo

def procesar_ronda(numero_ronda):
    subrondas = []
    ruta_archivo = obtener_ruta_ronda(numero_ronda)
    with open(ruta_archivo, "r") as ronda:
        for subronda in ronda:
            enemigos = procesar_subronda(subronda)
            subrondas.append(enemigos)
    return subrondas

def procesar_subronda(subronda):   
    enemigos = []
    oleada = subronda.split()
    for tipo_de_enemigo in oleada:
        enemigo = obtener_datos_enemigos(tipo_de_enemigo)
        enemigos.append(enemigo)
    return enemigos

def obtener_datos_enemigos(tipo):
    datos = enemigos[tipo]
    vida = datos["vida"]
    velocidad = datos["velocidad"]
    daño = datos["daño"]
    recompensa = datos["recompensa"]
    imagen = pg.image.load(datos["imagen"]).convert_alpha()
    
    return Enemy(world.waypoints, vida, velocidad, daño, recompensa, imagen)