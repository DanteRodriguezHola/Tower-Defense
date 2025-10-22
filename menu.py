import pygame as pg
from config import ventana

huergo = pg.image.load('assets/imagenes/huergo.png').convert_alpha()
fondo_menu = pg.image.load('assets/imagenes/menu/menu.png').convert_alpha()
jugar_img = pg.image.load('assets/imagenes/menu/boton_jugar.png').convert_alpha()
salir_img = pg.image.load('assets/imagenes/menu/boton_salir.png').convert_alpha()
jugar_hover = pg.image.load('assets/imagenes/menu/boton_jugar_hover.png').convert_alpha()
salir_hover = pg.image.load('assets/imagenes/menu/boton_salir_hover.png').convert_alpha()

class Boton:
    def __init__(self, x, y, imagen_normal, imagen_hover):
        self.imagen_normal = imagen_normal
        self.imagen_hover = imagen_hover
        self.rect = self.imagen_normal.get_rect(topleft=(x, y))
        self.hover = False

    def dibujar(self, pantalla):
        imagen = self.imagen_hover if self.hover else self.imagen_normal
        pantalla.blit(imagen, self.rect)

    def actualizar(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def click(self, evento):
        return evento.type == pg.MOUSEBUTTONDOWN and self.hover

# Crear botones una sola vez
boton_jugar = Boton(101, 270, jugar_img, jugar_hover)
boton_salir = Boton(165, 370, salir_img, salir_hover)

def menu():
    ventana.blit(fondo_menu, (0, 0))
    mouse_pos = pg.mouse.get_pos()

    boton_jugar.actualizar(mouse_pos)
    boton_salir.actualizar(mouse_pos)

    boton_jugar.dibujar(ventana)
    boton_salir.dibujar(ventana)

    ventana.blit(huergo, (0, 0))

    return boton_jugar, boton_salir