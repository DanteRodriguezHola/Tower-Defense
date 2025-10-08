import config as c
import enemy_list as e

import pygame as pg
import json

class World():
    def __init__(self, data, map_image):
        self.level = 1

        self.tile_map = []
        self.waypoints = []
        self.level_data = data
        self.image = map_image

        self.enemy_list = 0
        self.spawned_enemies = 0

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
        enemies = e.enemy_spawn_data[self.level - 1]
    


def cargar_mapa():
    mapa_imagen = pg.image.load('assets/imagenes/mapa.png').convert_alpha()
    with open('map.tmj') as file:
        world_data = json.load(file)
    world = World(world_data, mapa_imagen)
    world.process_data()
    return world