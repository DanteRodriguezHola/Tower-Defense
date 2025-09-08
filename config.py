from world import cargar_mapa
import pygame as pg

clock = pg.time.Clock()
ventana = pg.display.set_mode((700, 700))
world = cargar_mapa()

#Carga de elementos decorativos (titulo y icono del programa):
titulo = pg.display.set_caption("Stray Tower Defense")

icono_imagen = pg.image.load("assets\imagenes\icono.png").convert_alpha()
icono = pg.display.set_icon(icono_imagen)

#Estadisticas de los enemigos y torres:
enemigos = {
    "Nor": { #Zombie normal
        "vida": 5,
        "velocidad": 1.5,
        "daño": 1,
        "recompensa": 5,
        "imagen": "assets/imagenes/zombies/zombie_normal_nuevo.png",
        },
    "Len": { #Zombie lento, con mayor vida
        "vida": 25,
        "velocidad": 0.7,
        "daño": 3,
        "recompensa": 30,
        "imagen": "assets/imagenes/zombies/zombie_lento.png",
        },
    "Rap": { #Zombie rapido, con misma vida
        "vida": 5,
        "velocidad": 2.8,
        "daño": 3,
        "recompensa": 10,
        "imagen": "assets/imagenes/zombies/zombie_rapido.png",
        },
    "Jf1": { #Primer jefe, posee muchisima vida. Hace daño a la torre segun la vida que tenga en ese momento.
        "vida": 100,
        "velocidad": 1.3,
        "daño": "Igual a la vida final",
        "recompensa": 100,
        "imagen": "imagen",
        },
    "Mar": { #Zombie ligeramente más rapido
        "vida": 70,
        "velocidad": 2.1,
        "daño": 10,
        "recompensa": 70,
        "imagen": "la imagen",
        },
    "Base": { #Copia y pega
        "vida": 0,
        "velocidad": 0,
        "daño": 0,
        "recompensa": 0,
        "imagen": "imagen",
        },
}