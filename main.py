import config as c

from zombies import Enemy

from tienda import cargar_tienda

import torretas as t
import estadisticas as e
import botones as b
import pygame as pg

pg.init()
pg.font.init()

grupo_torretas = pg.sprite.Group()
grupo_enemigos = pg.sprite.Group()

#Variables que controlan el juego:
jugando = True

last_enemy_spawn = pg.time.get_ticks()
creando_torretas = False
torreta_seleccionada = None

text_font = pg.font.SysFont("Consolas", 40, bold =  True) 
large_font = pg.font.SysFont("Consolas", 52) 

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    c.ventana.blit(img, (x, y))

def mejorar_torreta(torreta_seleccionada):
    e.jugador["dinero"] -= torreta_seleccionada.upgrade_cost

    tipo_torreta = torreta_seleccionada.type
    nivel_torreta = torreta_seleccionada.upgrade_level + 1

    celda_x = torreta_seleccionada.tile_x
    celda_y = torreta_seleccionada.tile_y

    posicion_mouse = (celda_x, celda_y)

    t.crear_torreta(tipo_torreta, nivel_torreta, posicion_mouse, grupo_torretas)
    
nivel_torreta = 1

while jugando:
    c.clock.tick(60) 
    c.world.draw(c.ventana)
    cargar_tienda()

    #Actualizacion de los grupos
    for enemigo in grupo_enemigos:
        enemigo.update()
        enemigo.draw(c.ventana)
    
    for torreta in grupo_torretas:
        torreta.update(grupo_enemigos)
        torreta.draw(c.ventana)

    if torreta_seleccionada:
        torreta_seleccionada.selected = True

    cargar_tienda()

    if b.boton_tanque.draw(c.ventana):
        tipo_torreta = "Tanque"
        creando_torretas = True
    
    if b.boton_lanzallamas.draw(c.ventana):
        tipo_torreta = "Lanzallamas"
        creando_torretas = True

    if creando_torretas:
        if b.boton_cancelar.draw(c.ventana):
            creando_torretas = False

    if torreta_seleccionada != None:
        if torreta_seleccionada.upgrade_level < 3:
            if b.boton_mejora.draw(c.ventana):
                precio_mejora = (e.torretas[torreta_seleccionada.type])[torreta_seleccionada.upgrade_level]["precio"]
                if e.jugador["dinero"] >= precio_mejora:
                    torreta_seleccionada.mejorar_torreta()
                    e.jugador["dinero"] -= precio_mejora
                else:
                    print("¡No tienes suficiente dinero!")
        
        if b.boton_reembolso.draw(c.ventana):
            torreta_seleccionada = grupo_torretas.remove(torreta_seleccionada)
            e.jugador["dinero"] += torreta.refund
    
    #Aparición de enemigos
    if pg.time.get_ticks() - last_enemy_spawn > c.cooldown:
        if c.world.spawned_enemies < len(c.world.enemy_list):
            tipo_enemigo = c.world.enemy_list[c.world.spawned_enemies]
            enemigo = Enemy(tipo_enemigo, c.world.waypoints)
            grupo_enemigos.add(enemigo)
            c.world.spawned_enemies += 1
            last_enemy_spawn = pg.time.get_ticks()
    
    draw_text(str(e.jugador["vida"]), text_font, "grey100", 780, 605)
    draw_text(str(e.jugador["dinero"]), text_font, "grey100", 780, 668)

    if e.jugador["vida"] <= 0:
        jugando = False

    for evento in pg.event.get():
        #Al hacer click izquierdo
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
            #Si esta dentro del mapa, se crea una torreta
            if posicion_mouse[0] < c.ancho_mapa and posicion_mouse[1] < c.alto_mapa:
                torreta_seleccionada = None

                t.limpiar_seleccion(grupo_torretas)
                if creando_torretas:
                    t.crear_torreta(tipo_torreta, nivel_torreta, posicion_mouse, grupo_torretas)
                else:
                    torreta_seleccionada = t.seleccionar_torreta(posicion_mouse, grupo_torretas)
        #Salir del programa
        if evento.type == pg.QUIT:
            jugando = False
    pg.display.flip()
pg.quit()
