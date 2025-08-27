from zombies import Enemy
from world import World
import pygame as pg
import json

pg.init()

clock = pg.time.Clock()
ventana = pg.display.set_mode((570, 570))
titulo = pg.display.set_caption('Stray Tower Defense 😎')

#Carga de imagenes
zombie_img = pg.image.load('assets/imagenes/zombies/zombie1_normal.png').convert_alpha()
map_img = pg.image.load('assets/imagenes/mapa.png').convert_alpha()

with open('map.tmj') as file:
    world_data = json.load(file)

world = World(world_data, map_img)
world.process_data()

oleada = pg.sprite.Group()
enemigo = Enemy(world.waypoints, zombie_img)

jugando = True

while jugando:
    clock.tick(60)
    world.draw(ventana)
    oleada.add(enemigo)
    oleada.update()

    oleada.draw(ventana)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False
    pg.display.flip()

pg.quit()

if __name__ == "__main__":
    pass