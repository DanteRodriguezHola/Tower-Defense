from rondas import procesar_rondas

import random
import pygame as pg
import json

class World():
    def __init__(self, data, map_image):
        self.level = 0
        self.oleada = 1
        self.niveles_terminados = 0

        self.tile_map = []
        self.waypoints = []
        self.level_data = data
        self.image = map_image

        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

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

    """
    def terminar_ronda(self):
        self.niveles_terminados += 1
        print("world.py linea 43 niveles terminados:")
        print(self.niveles_terminados)
        if self.niveles_terminados == 5:
            print("world.py linea 46 self.oleada:")
            print("\n\n entre aca porque termino la ronda \n\n")
            self.oleada += 1
            self.niveles_terminados = 0
    """
    def check_level_complete(self):
        if (self.killed_enemies + self.missed_enemies) == len(self.enemy_list):
            print(self.killed_enemies)
            print(self.missed_enemies)
            print(len(self.enemy_list))
            #self.terminar_ronda()
            return True
        
    def reset_level(self):
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def process_enemies(self):
        enemy_spawn_data = procesar_rondas(self.oleada)
        try:
            enemies = enemy_spawn_data[self.level]
        except IndexError:
            self.level = 0
            self.oleada += 1
            enemies = enemy_spawn_data[self.level]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        random.shuffle(self.enemy_list)
"""crea una lista asi por ejemplo:
si te daba el diccionario asi: {"Nor" : 2, "Len" : 3}
te devuelve la lista enemy_list asi = ["Nor", "Nor", "Len", "Len", "Len"]
procesar_rondas
"""

def cargar_mapa():
    mapa_imagen = pg.image.load('assets/imagenes/mapa.png').convert_alpha()
    with open('map.tmj') as file:
        world_data = json.load(file)
    world = World(world_data, mapa_imagen)
    world.process_data()
    world.process_enemies()
    return world