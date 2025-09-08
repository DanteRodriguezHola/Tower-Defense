from config import ventana

import pygame as pg

class Torreta(pg.sprite.Sprite):
    def __init__(self, imagen, posicion):
        pg.sprite.Sprite.__init__(self)
        self.image = imagen #Se carga la imagen de la torreta
        self.rect = self.image.get_rect() #Se obtiene la hitbox de la torreta
        self.rect.center = posicion #Se obtiene la posicion de la torreta
    