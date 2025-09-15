import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, imagen, x , y):
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        posicion_mouse = pg.mouse.get_pos()

        if self.rect.collidepoint(posicion_mouse):
            if pg.mouse.get_pressed()[0] == 1:
                pass

        surface.blit(self.image, self.rect)
