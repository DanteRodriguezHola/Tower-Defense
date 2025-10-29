import estadisticas as e
import config as c

import math
import pygame as pg

class Torreta(pg.sprite.Sprite):
    def __init__(self, tipo_torreta, nivel_torreta, celda_x, celda_y):
        pg.sprite.Sprite.__init__(self)
        self.type = tipo_torreta
        self.upgrade_level = nivel_torreta
        

        estadisticas_torreta = e.torretas[self.type][self.upgrade_level - 1]

        self.damage = estadisticas_torreta["dano"]
        self.range = estadisticas_torreta["rango"]
        self.refund = (estadisticas_torreta["precio"]) // 5
        self.delay = estadisticas_torreta["espera"]

        self.selected = False

        self.last_shot = pg.time.get_ticks()

        #Posicion original
        self.tile_x = celda_x
        self.tile_y = celda_y

        #Calcular el centro de la celda
        self.x = (self.tile_x + 0.5) * c.tamano_celda
        self.y = (self.tile_y + 0.5) * c.tamano_celda
        
        #Se carga la imagen de la torreta
        self.original_image = pg.image.load(estadisticas_torreta["imagen"]).convert_alpha()
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
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
        surface.blit(self.image, self.rect)


    def update(self, grupo_enemigos):
        if pg.time.get_ticks() - self.last_shot > self.delay:
            self.elegir_objetivo(grupo_enemigos)

    def mejorar_torreta(self):
        self.upgrade_level += 1

        estadisticas_torreta = e.torretas[self.type][self.upgrade_level - 1]

        self.damage = estadisticas_torreta["dano"]
        self.range = estadisticas_torreta["rango"]
        self.refund = (estadisticas_torreta["precio"]) // 5
        self.delay = estadisticas_torreta["espera"]
        
        #Se carga la imagen de la torreta
        self.original_image = pg.image.load(estadisticas_torreta["imagen"]).convert_alpha()
        self.angle = 0
        self.image = pg.transform.rotate(self.original_image, self.angle)
        #Se obtiene la hitbox de la torreta
        self.rect = self.image.get_rect() 
        self.rect.center = (self.x, self.y)

        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)

        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def elegir_objetivo(self, grupo_enemigos):
        distancia_x = 0
        distancia_y = 0

        for enemigo in grupo_enemigos:
            if enemigo.health > 0:
                distancia_x = enemigo.pos[0] - self.x
                distancia_y = enemigo.pos[1] - self.y

                distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)

                if distancia < self.range:
                    self.target = enemigo
                    self.last_shot = pg.time.get_ticks()
                    self.angle = math.degrees(math.atan2(-distancia_y, distancia_x))
                    self.image = pg.transform.rotate(self.original_image, self.angle)
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                    self.target.health -= self.damage
                    print("Daño")

def crear_torreta(tipo_torreta, nivel_torreta, posicion_mouse, grupo_torretas):
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
            precio_torreta = e.torretas[tipo_torreta][nivel_torreta - 1]["precio"]
            if e.jugador["dinero"] >= precio_torreta:
                e.jugador["dinero"] -= precio_torreta
                torreta = Torreta(tipo_torreta, nivel_torreta, celda_x, celda_y)
                grupo_torretas.add(torreta)
                return True
        else:
            return False

def seleccionar_torreta(posicion_mouse, grupo_torretas):
    celda_x = posicion_mouse[0] // c.tamano_celda
    celda_y = posicion_mouse[1] // c.tamano_celda
    for torreta in grupo_torretas:
        if (celda_x,  celda_y) == (torreta.tile_x, torreta.tile_y):
            return torreta
        
def limpiar_seleccion(grupo_torretas):
    for torreta in grupo_torretas:
        torreta.selected = False