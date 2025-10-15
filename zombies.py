import config as c
from estadisticas import estadisticas_enemigos as estadisticas
from pygame.math import Vector2
import math

import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, enemy_type, waypoints): # Añadir: vida, velocidad, daño y recompensa.
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = estadisticas.get(enemy_type)["vida"]
        self.speed = estadisticas.get(enemy_type)["velocidad"]
        self.angle = 0
        self.original_image = pg.image.load(estadisticas.get(enemy_type)["imagen"]).convert_alpha()
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self):
        self.move()
        self.rotate()

    def move(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()

        dist = self.movement.length()
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1
    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos