import config as c
import const
from rondas import procesar_ronda
from torretas import crear_torreta, seleccionar_torreta
from tienda import cargar_tienda
from botones import Button
import pygame as pg
pg.init()
pg.font.init()

jugando = True
estado = "MENU"   # puede ser "MENU" o "JUEGO"

grupo_torretas = pg.sprite.Group()
subrondas = procesar_ronda("1")

grupo_enemigos = pg.sprite.Group()
for subronda in subrondas:
    grupo_enemigos.add(subronda)

# Variables que controlan el juego:
jugando = True
creando_torretas = False
torreta_seleccionada = None

text_font = pg.font.SysFont("Consolas", 40, bold =  True)
large_font = pg.font.SysFont("Consolas", 52)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    c.ventana.blit(img, (x, y))

while jugando:
    c.clock.tick(60)
    c.world.draw(c.ventana)
    cargar_tienda()

    # Actualización y dibujo de enemigos
    grupo_enemigos.update()
    for enemigo in grupo_enemigos:
        enemigo.draw(c.ventana)

    # Actualización y dibujo de torretas
    grupo_torretas.update(grupo_enemigos)

    if boton_tanque.draw(c.ventana):
        creando_torretas = True

    draw_text(str(c.world.health), text_font, "grey100", 780, 605)
    draw_text(str(c.world.money), text_font, "grey100", 780, 668)

    grupo_torretas.draw(c.ventana)
    for torreta in grupo_torretas:
        torreta.draw(c.ventana)

    for evento in pg.event.get():
        #Al hacer click izquierdo
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            posicion_mouse = pg.mouse.get_pos() #Se obtiene la posicion del ratón
            
            #Si se a pulsado el boton de la torreta
            if creando_torretas:
                #Si esta dentro del mapa, se crea una torreta
                if posicion_mouse[0] < c.ancho_mapa and posicion_mouse[1] < c.alto_mapa:
                    if const.costo_torreta < c.world.money and crear_torreta(posicion_mouse, grupo_torretas):
                        crear_torreta(posicion_mouse, grupo_torretas)
                        c.world.money -= const.costo_torreta
                else:
                    torreta_seleccionada = seleccionar_torreta(posicion_mouse, grupo_torretas)
        #Salir del programa
        if evento.type == pg.QUIT:
            jugando = False

    pg.display.flip()

pg.quit()

while jugando:
    clock.tick(60)
    ventana.fill((0, 0, 0))

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False

        if estado == "MENU":
            if boton_salir.click(evento):
                jugando = False
            if boton_jugar.click(evento):
                estado = "JUEGO"

    # Dibujar según estado
    if estado == "MENU":
        menu()
    elif estado == "JUEGO":
        world.draw(ventana)
        for subronda in subrondas:
            oleada = pg.sprite.Group()
            oleada.add(subronda)
            oleada.update()
            oleada.draw(ventana)

    pg.display.flip()

pg.quit()
