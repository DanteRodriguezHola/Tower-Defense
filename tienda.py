import config as c
import pygame as pg

tienda_imagen = pg.image.load("assets/imagenes/tienda/tienda.png").convert_alpha()

def cargar_tienda():
    c.ventana.blit(tienda_imagen, (c.ancho_mapa, 0))