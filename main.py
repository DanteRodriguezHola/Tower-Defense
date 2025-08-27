from zombies import Enemy
from world import World
import pygame as pg
import json


pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((570, 570))
pg.display.set_caption('Stray Tower Defense')

#Carga de imagenes
zombie_img = pg.image.load('assets/images/zombies/zombie1_normal.png').convert_alpha()
map_img = pg.image.load('assets/images/mapa.png').convert_alpha()

with open('map.tmj') as file:
    world_data = json.load(file)

world = World(world_data, map_img)
world.process_data()
enemy_group = pg.sprite.Group()


enemy = Enemy(world.waypoints, zombie_img)

jugando = True

while jugando:
    clock.tick(60)
    world.draw(screen)

    enemy_group.add(enemy)

    enemy_group.update()
    enemy_group.draw(screen)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False

    
    pg.display.flip()

pg.quit()