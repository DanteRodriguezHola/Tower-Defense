from config import pg
from rondas import procesar_rondas

import estadisticas as estadisticas
import random
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

    def check_level_complete(self):
        if (self.killed_enemies + self.missed_enemies) == len(self.enemy_list):
            return True
        
    def reset_level(self):
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def process_enemies(self):
        try:
            enemy_spawn_data = procesar_rondas(self.oleada)
            enemies = enemy_spawn_data[self.level]
        
        except IndexError:
            self.level = 0
            self.oleada += 1
            enemy_spawn_data = procesar_rondas(self.oleada)
            
            if not enemy_spawn_data:
                return
            
            enemies = enemy_spawn_data[self.level]
            
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)

        random.shuffle(self.enemy_list)

    def reiniciar_nivel(self, grupo_torretas, grupo_enemigos):
        self.level = -1
        self.oleada = 1
        self.niveles_terminados = 0

        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

        estadisticas.jugador["vida"] = 100
        estadisticas.jugador["dinero"] = 500

        for torreta in grupo_torretas:
            grupo_torretas.remove(torreta)

        for enemigo in grupo_enemigos:
            grupo_enemigos.remove(enemigo)
        

def cargar_mapa():
    imagen_mapa = pg.image.load('assets/imagenes/mapa.png').convert_alpha()
    with open('map.tmj') as file:
        world_data = json.load(file)
    world = World(world_data, imagen_mapa)
    world.process_data()
    world.process_enemies()
    return world

world = cargar_mapa()