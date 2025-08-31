from config import clock, ventana, world

from zombies import Enemy
from world import World
import pygame as pg
import json

#Carga de imagenes
zombie_img = pg.image.load('assets/imagenes/zombies/zombie_normal.png').convert_alpha()


oleada = pg.sprite.Group()
enemigo = Enemy(world.waypoints, zombie_img)

jugando = True

while jugando:
    clock.tick(60)
    world.draw(ventana)
    oleada.add(enemigo)
    oleada.add(enemigo)
    oleada.update()

    oleada.draw(ventana)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False
    pg.display.flip()

pg.quit()

if __name__ == "__main__":
    pass