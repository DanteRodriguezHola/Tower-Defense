# ------------------------------- #

# Importaciones #

from config import pg
from cursor import cursor
from menu import mostrar_menu
from tienda import cargar_tienda
from world import world
from zombies import Enemy

import config as c
import botones as b
import estadisticas as e
import manager as m
import torretas as t

# ------------------------------- #

grupo_torretas = pg.sprite.Group()
grupo_enemigos = pg.sprite.Group()
grupo_botones_torretas = pg.sprite.Group()
grupo_botones_torretas.add(b.boton_tanque)

text_font = pg.font.SysFont("Consolas", 40, bold =  True) 
large_font = pg.font.SysFont("Consolas", 56, bold =  True) 
small_font = pg.font.SysFont("Consolas", 16)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    c.ventana.blit(img, (x, y))

nivel_torreta = 1
tecla_presionada = None

while m.jugando:
    if m.estado == "menu":
        mostrar_menu(m.estado, grupo_torretas, grupo_enemigos)

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                m.jugando = False

        pg.display.flip()
    
    elif m.estado == "jugando":
        c.clock.tick(60) 
        world.draw(c.ventana)

    # ------------------------------- #

    # Actualizacion de las torretas y los enemigos #

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
            if boton.dibujar(c.ventana):
                tipo_torreta = boton.turret_type
                m.creando_torretas = True

        if b.boton_velocidad.dibujar(c.ventana):
            if not(b.boton_velocidad.clicked):
                m.velocidad_juego = 1
            else:
                m.velocidad_juego = 2
        
        if m.torreta_seleccionada:
            m.torreta_seleccionada.selected = True

        if m.creando_torretas:
            if b.boton_cancelar.dibujar(c.ventana):
                m.creando_torretas = False

        if m.torreta_seleccionada != None:
            if b.boton_mejorar.dibujar(c.ventana, m.torreta_seleccionada):
                m.torreta_seleccionada = t.mejorar_torreta(m.torreta_seleccionada, grupo_torretas)
                
            if b.boton_reembolsar.dibujar(c.ventana):
                m.torreta_seleccionada = m.torreta_seleccionada.reembolsar_torreta(grupo_torretas)

        if e.jugador["vida"] <= 0:
            e.jugador["vida"] = 0
            m.estado = "derrota"
        
        draw_text(str(e.jugador["vida"]), text_font, "black", 780, 605)
        draw_text(str(e.jugador["dinero"]), text_font, "black", 780, 668)

# ------------------------------- #

        if m.nivel_iniciado == False:
            if b.boton_comenzar.dibujar(c.ventana):
                m.nivel_iniciado = True
                m.tiempo_spawn_enemigos -= 10
        
        else:
            if pg.time.get_ticks() - m.ultimo_spawn_enemigo > (m.tiempo_spawn_enemigos / m.velocidad_juego):
                if world.spawned_enemies < len(world.enemy_list):
                    tipo_enemigo = world.enemy_list[world.spawned_enemies]
                    enemigo = Enemy(tipo_enemigo, world.waypoints)
                    grupo_enemigos.add(enemigo)
                    world.spawned_enemies += 1
                    m.ultimo_spawn_enemigo = pg.time.get_ticks()
        
        cursor.draw(c.ventana)

    # ------------------------------- #

        if world.check_level_complete() == True:
            world.level += 1
            m.ultimo_spawn_enemigo = pg.time.get_ticks()
            m.nivel_iniciado = False
            world.reset_level()
            world.process_enemies()

    # ------------------------------- #

    # Eventos #

        for evento in pg.event.get():

    # Al salir del programa #

            if evento.type == pg.QUIT:
                m.jugando = False

    # Al hacer click izquierdo # 

            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
                #Si esta dentro del mapa, se crea una torreta
                if posicion_mouse[0] < c.ancho_mapa and posicion_mouse[1] < c.alto_mapa:
                    m.torreta_seleccionada = None
                    t.limpiar_seleccion(grupo_torretas)
                    if m.creando_torretas:
                        t.crear_torreta(tipo_torreta, nivel_torreta, posicion_mouse, grupo_torretas)
                    else:
                        m.torreta_seleccionada = t.seleccionar_torreta(posicion_mouse, grupo_torretas)
            
    # Al presionar alguna tecla #

        mouse_pos = pg.mouse.get_pos()
        for enemigo in grupo_enemigos:
            enemigo.ver_info(mouse_pos, c.ventana)

        pg.display.flip()

    else:
        mostrar_menu(m.estado, grupo_torretas, grupo_enemigos)

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                m.jugando = False

        pg.display.flip()

pg.quit()