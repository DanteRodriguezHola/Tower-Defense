import config as c

from zombies import Enemy
from torretas import crear_torreta, seleccionar_torreta
from tienda import cargar_tienda
from botones import Button
import pygame as pg

#Carga de los botones
imagen_boton_tanque = pg.image.load("assets/imagenes/tienda/boton_tanque.png").convert_alpha()
boton_tanque = Button(imagen_boton_tanque, (c.ancho_mapa + c.ancho_tienda / 19), 180, True)

grupo_torretas = pg.sprite.Group()
grupo_enemigos = pg.sprite.Group()

#Variables que controlan el juego:
estado = "jugando"

last_enemy_spawn = pg.time.get_ticks()
creando_torretas = False
torreta_seleccionada = None

while estado == "jugando":
    c.clock.tick(60) 
    c.world.draw(c.ventana)
    cargar_tienda()
    #Actualizacion de los grupos
    for enemigo in grupo_enemigos:
        enemigo.update()
        enemigo.draw(c.ventana)

    grupo_torretas.update(grupo_enemigos)

    if boton_tanque.draw(c.ventana):
        creando_torretas = True

    grupo_torretas.draw(c.ventana)
    for torreta in grupo_torretas:
        torreta.draw(c.ventana)

    if pg.time.get_ticks() - last_enemy_spawn > c.cooldown:
        if c.world.spawned_enemies < len(c.world.enemy_list):
            tipo_enemigo = c.world.enemy_list[c.world.spawned_enemies]
            enemigo = Enemy(tipo_enemigo, c.world.waypoints)
            grupo_enemigos.add(enemigo)
            c.world.spawned_enemies += 1
            last_enemy_spawn = pg.time.get_ticks()

    for evento in pg.event.get():
        #Al hacer click izquierdo
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
            
            #Si se a pulsado el boton de la torreta
            if creando_torretas:
                #Si esta dentro del mapa, se crea una torreta
                if posicion_mouse[0] < c.ancho_mapa and posicion_mouse[1] < c.alto_mapa:
                    crear_torreta(posicion_mouse, grupo_torretas)
                else:
                    torreta_seleccionada = seleccionar_torreta(posicion_mouse, grupo_torretas)
            
        #Salir del programa
        if evento.type == pg.QUIT:
            jugando = False
    pg.display.flip()
            
           
pg.quit()

if __name__ == "__main__":
    pass