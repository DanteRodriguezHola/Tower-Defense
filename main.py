# ------------------------------- #

# Importaciones #

import config as c

from zombies import Enemy

from tienda import cargar_tienda

import torretas as t
import estadisticas as e
import botones as b
import pygame as pg

# ------------------------------- #

pg.init()
pg.font.init()

grupo_torretas = pg.sprite.Group()
grupo_enemigos = pg.sprite.Group()

grupo_botones_torretas = pg.sprite.Group()

grupo_botones_torretas.add(b.boton_tanque, b.boton_explosivos)

#Variables que controlan el juego:
jugando = True

last_enemy_spawn = pg.time.get_ticks()
level_started = False
creando_torretas = False
torreta_seleccionada = None

text_font = pg.font.SysFont("Consolas", 40, bold =  True) 
large_font = pg.font.SysFont("Consolas", 52) 

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    c.ventana.blit(img, (x, y))

def mejorar_torreta_seleccionada(torreta_seleccionada):
    if torreta_seleccionada.upgrade_level >= 3:
        return
    
    if not(b.boton_mejorar.draw(c.ventana)):
        return
    
    precio_mejora = (e.torretas[torreta_seleccionada.type])[torreta_seleccionada.upgrade_level]["precio"]
    
    if e.jugador["dinero"] < precio_mejora:
        return
    
    torreta_seleccionada.mejorar_torreta()
    e.jugador["dinero"] -= precio_mejora

nivel_torreta = 1
tecla_presionada = None

while jugando:
    c.clock.tick(60) 
    c.world.draw(c.ventana)

    # ------------------------------- #

    # Actualizacion de los grupos #

    for enemigo in grupo_enemigos:
        enemigo.update()
        enemigo.draw(c.ventana)
    
    for torreta in grupo_torretas:
        torreta.update(grupo_enemigos)
        torreta.draw(c.ventana)

    # ------------------------------- #
    
    # Actualizacion de la tienda y los botones #

    cargar_tienda()

    for boton in grupo_botones_torretas:
        if boton.draw(c.ventana) or tecla_presionada == boton.hotkey:
            print(boton)
            tipo_torreta = "Tanque"
            creando_torretas = True

    if torreta_seleccionada:
        torreta_seleccionada.selected = True

    if creando_torretas:
        if b.boton_cancelar.draw(c.ventana) or tecla_presionada == c.atajo_cancelar_reembolso:
            creando_torretas = False
            

    if not(torreta_seleccionada == None):
        mejorar_torreta_seleccionada(torreta_seleccionada)
        
        if b.boton_reembolsar.draw(c.ventana) or tecla_presionada == c.atajo_cancelar_reembolso:
            torreta_seleccionada = grupo_torretas.remove(torreta_seleccionada)
            e.jugador["dinero"] += torreta.refund

    if level_started == False:
        if b.boton_comenzar.draw(c.ventana) or tecla_presionada == c.atajo_comenzar:
            level_started = True
            
    draw_text(str(e.jugador["vida"]), text_font, "grey100", 780, 605)
    draw_text(str(e.jugador["dinero"]), text_font, "grey100", 780, 668)

    # ------------------------------- #

    if level_started == False:
        if b.boton_comenzar.draw(c.ventana) or tecla_presionada == c.atajo_comenzar:
            level_started = True
    
    else:
        if pg.time.get_ticks() - last_enemy_spawn > c.cooldown:
            if c.world.spawned_enemies < len(c.world.enemy_list):
                tipo_enemigo = c.world.enemy_list[c.world.spawned_enemies]
                enemigo = Enemy(tipo_enemigo, c.world.waypoints)
                grupo_enemigos.add(enemigo)
                c.world.spawned_enemies += 1
                last_enemy_spawn = pg.time.get_ticks()

    # ------------------------------- #

    # Trampas de desarollador #

    if tecla_presionada == 43:
        e.jugador["dinero"] += 100

    if tecla_presionada == 45:
        e.jugador["dinero"] -= 100

    if tecla_presionada == 1073742053:
        for enemigo in grupo_enemigos:
            enemigo.pygame.sprite.kill()

    # ------------------------------- #
    tecla_presionada = None

    if c.world.check_level_complete() == True:
        c.world.level += 1
        last_enemy_spawn = pg.time.get_ticks()
        level_started = False
        c.world.reset_level()
        c.world.process_enemies()

    if e.jugador["vida"] <= 0:
        jugando = False
        print("¡Perdiste!")

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False

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

        if evento.type == pg.KEYDOWN:
            tecla_presionada = evento.key
            print(tecla_presionada)

    pg.display.flip()

    
pg.quit()
