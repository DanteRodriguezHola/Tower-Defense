import config as c
import pygame as pg

text_font = pg.font.SysFont("Consolas", 40, bold =  True) 
large_font = pg.font.SysFont("Consolas", 56, bold =  True) 
small_font = pg.font.SysFont("Consolas", 16)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    c.ventana.blit(img, (x, y))