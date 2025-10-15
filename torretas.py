import config as c

import math
import pygame as pg

class Torreta(pg.sprite.Sprite):
    def __init__(self, imagen, celda_x, celda_y):
        pg.sprite.Sprite.__init__(self)
        #Estadisticas de la torre
        self.range = 120
        self.delay = 500
        self.selected = False

        self.last_shot = pg.time.get_ticks()

        #Posicion original
        self.tile_x = celda_x
        self.tile_y = celda_y

        #Calcular el centro de la celda
        self.x = (self.tile_x + 0.5) * c.tamano_celda
        self.y = (self.tile_y + 0.5) * c.tamano_celda
        
        #Se carga la imagen de la torreta
        self.original_image = imagen
        self.angle = 0
        self.image = pg.transform.rotate(self.original_image, self.angle)
        #Se obtiene la hitbox de la torreta
        self.rect = self.image.get_rect() 
        self.rect.center = (self.x, self.y)

        
        #Se crea un circulo transparente mostrando el rango de ataque
        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)

        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    def update(self, grupo_enemigos):
        if pg.time.get_ticks() - self.last_shot > self.delay:
            self.elegir_objetivo(grupo_enemigos)

    def elegir_objetivo(self, grupo_enemigos):
        distancia_x = 0
        distancia_y = 0

        for enemigo in grupo_enemigos:
            distancia_x = enemigo.pos[0] - self.x
            distancia_y = enemigo.pos[1] - self.y

            distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)

            if distancia < self.range:
                self.target = enemigo
                self.angle = math.degrees(math.atan2(-distancia_y, distancia_x))

def crear_torreta(posicion_mouse, grupo_torretas):
    imagen_torreta = pg.image.load("assets/imagenes/torretas/torretas_HD/torreta_tanque.png").convert_alpha()
    
    celda_x = posicion_mouse[0] // c.tamano_celda
    celda_y = posicion_mouse[1] // c.tamano_celda
    celda_numero = (celda_y * 15) + celda_x

    #Se comprueba si donde se va a colocar la torreta esta fuera del sendero.
    if c.world.tile_map[celda_numero] == 7: 
        espacio_libre = True
        #Esto comprueba si donde esta ubicado el mouse ya hay otra torreta.
        for torreta in grupo_torretas:
            if (celda_x,  celda_y) == (torreta.tile_x, torreta.tile_y):
                espacio_libre = False
        #Se crea la torreta.
        if espacio_libre:
            torreta = Torreta(imagen_torreta, celda_x, celda_y)   # 30
            grupo_torretas.add(torreta)

def seleccionar_torreta(posicion_mouse, grupo_torretas):
    celda_x = posicion_mouse[0] // c.tamano_celda
    celda_y = posicion_mouse[1] // c.tamano_celda
    for torreta in grupo_torretas:
        if (celda_x,  celda_y) == (torreta.tile_x, torreta.tile_y):
            return torreta
        
def limpiar_seleccion(grupo_torretas):
    for torreta in grupo_torretas:
        torreta.selected = False