from config import world, tamano_celda

import pygame as pg

class Torreta(pg.sprite.Sprite):
    def __init__(self, imagen, celda_x, celda_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = celda_x
        self.tile_y = celda_y
        self.x = (self.tile_x + 0.5) * tamano_celda
        self.y = (self.tile_y + 0.5) * tamano_celda
        self.image = imagen #Se carga la imagen de la torreta
        self.rect = self.image.get_rect() #Se obtiene la hitbox de la torreta
        self.rect.center = (self.x, self.y)
    
def crear_torreta(posicion_mouse, grupo_torretas):
    imagen_torreta = pg.image.load("assets/imagenes/torretas/torreta_tanque_chica.png").convert_alpha()
    
    celda_x = posicion_mouse[0] // tamano_celda
    celda_y = posicion_mouse[1] // tamano_celda
    celda_numero = (celda_y * 30) + celda_x

    #Se comprueba si donde se va a colocar la torreta esta fuera del sendero.
    if world.tile_map[celda_numero] == 16: 
        espacio_libre = True
        #Esto comprueba si donde esta ubicado el mouse ya hay otra torreta.
        for torreta in grupo_torretas:
            if (celda_x,  celda_y) == (torreta.tile_x, torreta.tile_y):
                espacio_libre = False
        #Se crea la torreta.
        if espacio_libre:
            torreta = Torreta(imagen_torreta, celda_x, celda_y)   # 30
            grupo_torretas.add(torreta)
