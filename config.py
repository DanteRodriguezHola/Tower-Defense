from world import cargar_mapa
import pygame as pg

#Carga el reloj
clock = pg.time.Clock()

#Definicion las dimesiones de la ventana
ancho_mapa = 720
alto_mapa = 720

tamano_celda = 48

ancho_tienda = 260

#Tamaño de la ventana total: 850 x 980
ventana = pg.display.set_mode((ancho_mapa + ancho_tienda, alto_mapa)) 

world = cargar_mapa()

#Carga de elementos decorativos (titulo y icono del programa)
titulo = pg.display.set_caption("Stray Tower Defense")

icono_imagen = pg.image.load("assets\imagenes\icono.png").convert_alpha()
icono = pg.display.set_icon(icono_imagen)