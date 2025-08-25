import pygame

pygame.init()

#Definiendo nuestras variables
ventana = (600, 900)
clock = pygame.time.Clock()
titulo = pygame.display.set_caption("Stray Tower Defense")
jugando = True

#Loop de juego básico
while jugando:
    pygame.display.set_mode(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           jugando = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()