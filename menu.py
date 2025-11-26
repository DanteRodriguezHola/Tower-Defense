from config import pg
from cursor import cursor
from spritesheet import Spritesheet
from world import world

import botones as b
import config as c
import manager as m

spritesheet_menu = Spritesheet("assets/imagenes/menu/spritesheet_menu.png")

imagenes_menu = {
    "menu": 0,
    "derrota": 720,
    "victoria": 1440,
}

for imagen in imagenes_menu:
    imagenes_menu[imagen] = spritesheet_menu.obtener_imagen(c.ancho_ventana, c.alto_ventana, 0, imagenes_menu[imagen])

def mostrar_menu(estado, grupo_torretas, grupo_enemigos):
    c.ventana.blit(imagenes_menu[estado], (0, 0))

    if m.estado == "menu":
        if b.boton_jugar.dibujar(c.ventana):
            m.estado = "jugando"
    
    else:
         if b.boton_reintentar.dibujar(c.ventana):
            world.reiniciar_nivel(grupo_torretas, grupo_enemigos)
            m.estado = "jugando"         

    if b.boton_salir.dibujar(c.ventana):
        m.jugando = False

    cursor.draw(c.ventana)