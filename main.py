from config import clock, ventana, world

from rondas import procesar_ronda
import pygame as pg
import json

grupo_enemigos = procesar_ronda()
oleada = pg.sprite.Group()
oleada.add(grupo_enemigos)

jugando = True

while jugando:
    clock.tick(60)
    world.draw(ventana)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False
    pg.display.flip()

pg.quit()

if __name__ == "__main__":
    pass