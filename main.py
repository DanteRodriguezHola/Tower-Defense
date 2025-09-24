from config import clock, ventana, world

from rondas import procesar_ronda
from torretas import crear_torreta

import pygame as pg

jugando = True

grupo_torretas = pg.sprite.Group()
subrondas = procesar_ronda("1")

while jugando:
    clock.tick(60) 
    world.draw(ventana)
    for subronda in subrondas:
        oleada = pg.sprite.Group()
        oleada.add(subronda)
        oleada.update()
        oleada.draw(ventana)
        grupo_torretas.draw(ventana)
        
        for evento in pg.event.get():
            #Al hacer click izquierdo
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
                if posicion_mouse[0] < 720 and posicion_mouse[1] < 720:
                    crear_torreta(posicion_mouse, grupo_torretas)
            #Salir del programa
            if evento.type == pg.QUIT:
                jugando = False

        pg.display.flip()
pg.quit()

if __name__ == "__main__":
    pass