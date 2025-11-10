import pygame as pg

class Spritesheet:
    def __init__(self, imagen):
        self.spritesheet = pg.image.load(imagen).convert_alpha()

    def obtener_imagen(self, ancho, alto, posicion_x, posicion_y):
        imagen = pg.Surface((ancho, alto), pg.SRCALPHA)
        imagen.blit(self.spritesheet, (0, 0), (posicion_x, posicion_y, ancho, alto))

        return imagen