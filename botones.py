import config as c
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


# ------------------------------- #

# Carga de imagenes y creación de los botones #

imagen_boton_tanque = pg.image.load("assets/imagenes/tienda/boton_tanque.png").convert_alpha()
imagen_boton_tanque_hover = pg.image.load("assets/imagenes/tienda/boton_tanque_hover.png").convert_alpha()
boton_tanque = Button(imagen_boton_tanque, imagen_boton_tanque_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_1, True)

imagen_boton_dinamita = pg.image.load("assets/imagenes/tienda/boton_dinamita.png").convert_alpha()
imagen_boton_dinamita_hover = pg.image.load("assets/imagenes/tienda/boton_dinamita_hover.png").convert_alpha()
boton_lanzallamas = Button(imagen_boton_dinamita, imagen_boton_dinamita_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_2, True)

imagen_boton_cancelar = pg.image.load("assets/imagenes/tienda/boton_cancelar.png").convert_alpha()
imagen_boton_cancelar_hover = pg.image.load("assets/imagenes/tienda/boton_cancelar_hover.png").convert_alpha()
boton_cancelar = Button(imagen_boton_cancelar, imagen_boton_cancelar_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_6, True)

imagen_boton_mejora = pg.image.load("assets/imagenes/tienda/boton_mejora.png").convert_alpha()
imagen_boton_mejora_hover = pg.image.load("assets/imagenes/tienda/boton_mejora_hover.png").convert_alpha()
boton_mejora = Button(imagen_boton_mejora, imagen_boton_mejora_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_5, True)

imagen_boton_reembolso = pg.image.load("assets/imagenes/tienda/boton_reembolso.png").convert_alpha()
imagen_boton_reembolso_hover = pg.image.load("assets/imagenes/tienda/boton_reembolso_hover.png").convert_alpha()
boton_reembolso = Button(imagen_boton_reembolso, imagen_boton_reembolso_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_6, True)

imagen_boton_comenzar = pg.image.load("assets/imagenes/tienda/boton_comenzar.png").convert_alpha()
imagen_boton_comenzar_hover = pg.image.load("assets/imagenes/tienda/boton_comenzar_hover.png").convert_alpha()
boton_comenzar = Button(imagen_boton_comenzar, imagen_boton_comenzar_hover, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_5_a, True)

# ------------------------------- #