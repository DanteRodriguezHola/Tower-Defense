import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, imagen, imagen_hover, x , y, single_click):
        self.image = imagen
        self.image_hov = imagen_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click
    def draw(self, surface):
        accion = False
        posicion_mouse = pg.mouse.get_pos()

        if self.rect.collidepoint(posicion_mouse):
            # CAPAZ ESTOY MAL, HAY Q VER---------
            surface.blit(self.image_hov, self.rect)
            # mi proceso-------------
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                accion = True

                if self.single_click:
                    self.clicked = True
        else:
            surface.blit(self.image, self.rect)

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return accion
