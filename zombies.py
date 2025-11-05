import estadisticas as e
import config as c

from pygame.math import Vector2
import math

import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, enemy_type, waypoints): # Añadir: vida, velocidad, daño y recompensa.
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        
        self.health = e.enemigos.get(enemy_type)["vida"]
        self.damage = e.enemigos.get(enemy_type)["dano"]
        self.speed = e.enemigos.get(enemy_type)["velocidad"]
        self.reward = e.enemigos.get(enemy_type)["recompensa"]

        self.angle = 0
        self.original_image = pg.image.load(e.enemigos.get(enemy_type)["imagen"]).convert_alpha()
        self.auch_image = pg.image.load(e.enemigos.get(enemy_type)["imagen_auch"]).convert_alpha()
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.is_hurt = False
        self.hurt_time = 0
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self):
        self.move()
        self.rotate()
        self.check_alive()
        self.update_hurt_state()
    
    def update_hurt_state(self):
        if self.is_hurt:
            if pg.time.get_ticks() - self.hurt_time < 150:
                self.image = pg.transform.rotate(self.auch_image, self.angle)
            else:
                self.image = pg.transform.rotate(self.original_image, self.angle)
                self.is_hurt = False

    def move(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            e.jugador["vida"] -= self.damage
            c.world.missed_enemies += 1
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

    def check_alive(self):
        if self.health <= 0:
            c.world.killed_enemies += 1
            e.jugador["dinero"] += self.reward
            self.kill()
    
    def take_damage(self, amount):
        self.health -= amount
        self.is_hurt = True
        self.hurt_time = pg.time.get_ticks()