from config import clock, ventana, world
from rondas import procesar_ronda
from menu import menu, boton_jugar, boton_salir
import pygame as pg

jugando = True
subrondas = procesar_ronda("1")

while jugando:
    clock.tick(60)
    ventana.fill((0, 0, 0))

    boton_jugar, boton_salir = menu()

    for evento in pg.event.get():
        if evento.type == pg.QUIT or boton_salir.click(evento):
            jugando = False
        if boton_jugar.click(evento):
            print("¡Jugar presionado!")

    world.draw(ventana)
    for subronda in subrondas:
        oleada = pg.sprite.Group()
        oleada.add(subronda)
        oleada.update()
        oleada.draw(ventana)

    pg.display.flip()

pg.quit()