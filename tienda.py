import config as c
import pygame as pg

def cargar_tienda():
    tienda_imagen = pg.image.load("assets/imagenes/tienda/tienda.png").convert_alpha()
    c.ventana.blit(tienda_imagen, (c.ancho_mapa, 0))