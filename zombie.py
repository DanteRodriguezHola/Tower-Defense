from pygame.math import Vector2
import pygame, math

def movimiento(waypoints):
    posicion = Vector2(waypoints[0])
    velocidad = 2
    target = 1
    if target < len(waypoints):
        target = Vector2(waypoints[target])
        mov = target - posicion
    else:
        
    