from mapa import leer_waypoints, procesar_waypoints
import pygame

pygame.init()

#Definiendo nuestras variables
ventana = pygame.display.set_mode((570, 570))
clock = pygame.time.Clock()
titulo = pygame.display.set_caption("Stray Tower Defense")
jugando = True

#Carga de imagenes
zombie_img = pygame.image.load("assets/images/zombies/zombie1_normal.png").convert_alpha()
zombie_lento_img = pygame.image.load("assets/images/zombies/zombie2_lento.png").convert_alpha()
zombie_rapido_img = pygame.image.load("assets/images/zombies/zombie3_rapido.png").convert_alpha()
mapa_img = pygame.image.load("assets/images/mapa.png").convert_alpha()

#Loop de juego básico
while jugando:
    ventana.blit(mapa_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           jugando = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()