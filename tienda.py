from config import ventana
import pygame as pg

def cargar_tienda():
    tienda_imagen = pg.image.load("assets/imagenes/tienda.png").convert_alpha()
    ventana.blit(tienda_imagen, (0,0))