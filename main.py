from config import clock, ventana, world
from tienda import cargar_tienda
from rondas import procesar_ronda

import pygame as pg

jugando = True

subrondas = procesar_ronda("1")
while jugando:
    clock.tick(60)
    world.draw(ventana)
    cargar_tienda()
    for subronda in subrondas:
        oleada = pg.sprite.Group()
        oleada.add(subronda)
        oleada.update()
        oleada.draw(ventana)        
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                jugando = False
                break
        pg.display.flip()
pg.quit()

if __name__ == "__main__":
    pass