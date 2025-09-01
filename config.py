from world import cargar_mapa
import pygame as pg

clock = pg.time.Clock()
ventana = pg.display.set_mode((570, 570))
world = cargar_mapa()

titulo = pg.display.set_caption("Stray Tower Defense")
icono = pg.display.set_icon(pg.image.load("assets\imagenes\icono.png").convert_alpha())


enemigos = {
    "Nor": {
        "vida": 5,
        "velocidad": 1.5,
        "daño": 1,
        "recompensa": 5,
        "imagen": "assets/imagenes/zombies/zombie_normal.png",
        },
    "Len": {
        "vida": 30,
        "velocidad": 0.7,
        "daño": 3,
        "recompensa": 30,
        "imagen": "assets/imagenes/zombies/zombie_len.png",
        },
    "Rap": {
        "vida": 10,
        "velocidad": 2.8,
        "daño": 3,
        "recompensa": 10,
        "imagen": "assets/imagenes/zombies/zombie_rapido.png",
        },
    "Jf1": {
        "vida": 100,
        "velocidad": 1.5,
        "daño": "Igual a la vida final",
        "recompensa": 100,
        "imagen": "imagen",
        },
    "Mar": {
        "vida": 70,
        "velocidad": 3,
        "daño": 10,
        "recompensa": 70,
        "imagen": "la imagen",
        },
    "Xyz": {
        "vida": 0,
        "velocidad": 0,
        "daño": 0,
        "recompensa": 0,
        "imagen": "imagen",
        },
}