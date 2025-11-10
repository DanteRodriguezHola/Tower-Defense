from spritesheet import Spritesheet

import config as c
import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, imagenes, atajo_teclado, x , y, single_click):
        pg.sprite.Sprite.__init__(self)

        # ------------------------------- #

        self.image_normal = imagenes.get("normal")
        self.image_hover = imagenes.get("hover")
        self.image_blocked = imagenes.get("bloqueado")

        # ------------------------------- #

        self.hotkey = atajo_teclado

        self.rect = self.image_normal.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click
    
    def draw(self, surface):
        accion = False
        posicion_mouse = pg.mouse.get_pos()

        if self.rect.collidepoint(posicion_mouse):
            surface.blit(self.image_hover, self.rect)
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                accion = True

                if self.single_click:
                    self.clicked = True
        else:
            surface.blit(self.image_normal, self.rect)

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return accion

# ------------------------------- #

# Carga de imagenes y creación de los botones #

spritesheet_boton_tanque = Spritesheet("assets/imagenes/tienda/spritesheet_boton_tanque.png")

imagenes_boton_tanque = {
    "normal": spritesheet_boton_tanque.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_tanque.obtener_imagen(240, 52, 0, 52),
    "bloqueado": spritesheet_boton_tanque.obtener_imagen(240, 52, 0, 104),
}

boton_tanque = Button(imagenes_boton_tanque, c.atajo_tanque, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_1, True)

spritesheet_boton_explosivos = Spritesheet("assets/imagenes/tienda/spritesheet_boton_explosivos.png")

imagenes_boton_explosivos = {
    "normal": spritesheet_boton_explosivos.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_explosivos.obtener_imagen(240, 52, 0, 52),
    "bloqueado": spritesheet_boton_explosivos.obtener_imagen(240, 52, 0, 104),
}

boton_explosivos = Button(imagenes_boton_explosivos, c.atajo_explosivos, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_2, True)

spritesheet_boton_comenzar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_comenzar.png")

imagenes_boton_comenzar = {
    "normal": spritesheet_boton_comenzar.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_comenzar.obtener_imagen(240, 52, 0, 52),
    "bloqueado": spritesheet_boton_comenzar.obtener_imagen(240, 52, 0, 104),
}

boton_comenzar = Button(imagenes_boton_comenzar, c.atajo_comenzar, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_5_a, True)

spritesheet_boton_mejorar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_mejorar.png")

imagenes_boton_mejorar = {
    "normal": spritesheet_boton_mejorar.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_mejorar.obtener_imagen(240, 52, 0, 52),
}

boton_mejorar = Button(imagenes_boton_mejorar, c.atajo_mejorar, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_5, True)

spritesheet_boton_cancelar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_cancelar.png")

imagenes_boton_cancelar = {
    "normal": spritesheet_boton_cancelar.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_cancelar.obtener_imagen(240, 52, 0, 52),
}

boton_cancelar = Button(imagenes_boton_cancelar, c.atajo_cancelar_reembolso, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_6, True)

spritesheet_boton_reembolsar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_reembolsar.png")

imagenes_boton_reembolsar = {
    "normal": spritesheet_boton_reembolsar.obtener_imagen(240, 52, 0, 0),
    "hover": spritesheet_boton_reembolsar.obtener_imagen(240, 52, 0, 52),
}

boton_reembolsar = Button(imagenes_boton_reembolsar, c.atajo_cancelar_reembolso, (c.ancho_mapa + c.ancho_tienda / 19), c.pos_6, True)

# ------------------------------- #