from config import ventana, world, enemigos
from zombies import Enemy

import pygame as pg

def procesar_oleada(oleada):   
    grupo_enemigos = []
    enemigos_presentes = oleada.split()
    for tipo_de_enemigo in enemigos_presentes:
        enemigo = obtener_datos_enemigos(tipo_de_enemigo)
        grupo_enemigos.append(enemigo)
    return grupo_enemigos

def obtener_datos_enemigos(tipo):
    datos = enemigos[tipo]
    vida = datos["vida"]
    velocidad = datos["velocidad"]
    daño = datos["daño"]
    recompensa = datos["recompensa"]
    imagen = pg.image.load(datos["imagen"]).convert_alpha()
    return Enemy(world.waypoints, vida, velocidad, daño, recompensa, imagen)

def movimiento(oleada):
    grupo_enemigos = procesar_oleada(oleada)
    oleada = pg.sprite.Group(grupo_enemigos)
    
    while bool(oleada):
        oleada.update()
        oleada.draw(ventana)