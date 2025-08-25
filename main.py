import pygame as pg
import json
from world import World
from zombies import Enemy

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((30*19, 30*19))
pg.display.set_caption('pene rico rico')

#imagenes jiij
zombie_img = pg.image.load('assets/images/zombies/zombie1_normal.png').convert_alpha()
map_img = pg.image.load('assets/images/mapa.png').convert_alpha()

with open('map.tmj') as file:
    world_data = json.load(file)

world = World(world_data, map_img)
world.process_data()
enemy_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, zombie_img)
enemy_group.add(enemy)

game_over = False
while not game_over:
    clock.tick(60)

    screen.fill('grey100')
    world.draw(screen)
    
    enemy_group.update()

    enemy_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    pg.display.flip()

pg.quit()