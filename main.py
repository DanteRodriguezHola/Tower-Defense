from config import clock, ventana, world
from rondas import procesar_ronda
from menu import menu, boton_jugar, boton_salir
import pygame as pg

jugando = True
estado = "MENU"   # puede ser "MENU" o "JUEGO"

subrondas = procesar_ronda("1")

while jugando:
    clock.tick(60)
    ventana.fill((0, 0, 0))

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jugando = False

        if estado == "MENU":
            if boton_salir.click(evento):
                jugando = False
            if boton_jugar.click(evento):
                print("¡Jugar presionado!")
                estado = "JUEGO"

    # Dibujar según estado
    if estado == "MENU":
        menu()
    elif estado == "JUEGO":
        world.draw(ventana)
        for subronda in subrondas:
            oleada = pg.sprite.Group()
            oleada.add(subronda)
            oleada.update()
            oleada.draw(ventana)

    pg.display.flip()

pg.quit()
