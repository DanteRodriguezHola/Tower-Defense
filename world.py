import estadisticas as e
from rondas import procesar_rondas

import random
import pygame as pg
import json

class World():
    def __init__(self, data, map_image):
        self.level = 1

        self.tile_map = []
        self.waypoints = []
        self.level_data = data
        self.image = map_image

        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0
        
        self.oleada = 0

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        
    def process_data(self):
        for layer in self.level_data["layers"]:
            if layer["name"] == "tilemap":
                self.tile_map = layer["data"]
            elif layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)
    
    def process_waypoints(self, data):
        for punto in data:
            temp_x = punto.get('x')
            temp_y = punto.get('y')
            self.waypoints.append((temp_x, temp_y))

    def process_enemies(self):
        try: #no se
            enemy_spawn_data = procesar_rondas(self.level)
            enemies = enemy_spawn_data[self.oleada]
        except:
            print("No se pudo cargar la ronda")
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)
    
    def check_level_complete(self):
        if (self.killed_enemies + self.missed_enemies) == len(self.enemy_list):
            return True
        
    def reset_level(self):
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

def cargar_mapa():
    mapa_imagen = pg.image.load('assets/imagenes/mapa.png').convert_alpha()
    with open('map.tmj') as file:
        world_data = json.load(file)
    world = World(world_data, mapa_imagen)
    world.process_data()
    world.process_enemies()
    return world