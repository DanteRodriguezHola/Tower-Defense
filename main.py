import config as c

from rondas import procesar_ronda
from torretas import crear_torreta
from tienda import cargar_tienda
from botones import Button
import pygame as pg

jugando = True

#Carga de los botones
imagen_boton_tanque = pg.image.load("assets/imagenes/tienda/boton_tanque.png").convert_alpha()
boton_tanque = Button(imagen_boton_tanque, (c.ancho_mapa + c.ancho_tienda / 19), 180, True)

grupo_torretas = pg.sprite.Group()
subrondas = procesar_ronda("1")

creando_torretas = False

while jugando:
    c.clock.tick(60) 
    c.world.draw(c.ventana)
    cargar_tienda()
    for subronda in subrondas:
        oleada = pg.sprite.Group()
        oleada.add(subronda)
        oleada.update()
        oleada.draw(c.ventana)
        if boton_tanque.draw(c.ventana):
            creando_torretas = True

        grupo_torretas.draw(c.ventana)
        
        for evento in pg.event.get():
            #Al hacer click izquierdo
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
                
                #Si se a pulsado el boton de la torreta
                if creando_torretas:
                    #Si esta dentro del mapa, se crea una torreta
                    if posicion_mouse[0] < c.ancho_mapa and posicion_mouse[1] < c.alto_mapa:
                        crear_torreta(posicion_mouse, grupo_torretas)
                
            #Salir del programa
            if evento.type == pg.QUIT:
                jugando = False

        pg.display.flip()
pg.quit()

if __name__ == "__main__":
    pass