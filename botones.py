from spritesheet import Spritesheet

import config as c
import pygame as pg
import estadisticas as e

class Button(pg.sprite.Sprite):
    def __init__(self, spritesheet, atajo_teclado, x , y, single_click):
        pg.sprite.Sprite.__init__(self)

        self.images = {
            "normal": "",
            "hover": "",
            "blocked": "",
        }

        numero = 0

        for image in self.images:
            self.images[image] = spritesheet.obtener_imagen(c.ancho_boton, c.alto_boton, 0, numero)
            numero += 52

        # ------------------------------- #

        self.hotkey = atajo_teclado

        self.rect = self.images["normal"].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click
    
    def draw(self, surface, pressed_key):
        posicion_mouse = pg.mouse.get_pos()
        accion = False
        
        if not(self.rect.collidepoint(posicion_mouse) or pressed_key == self.hotkey):
            surface.blit(self.images["normal"], self.rect)
            return accion
        
        surface.blit(self.images["hover"], self.rect)
        
        if ((pg.mouse.get_pressed()[0] == 1 and self.clicked == False) or pressed_key == self.hotkey):
            accion = True

            if self.single_click:
                self.clicked = True
                
            return accion

        self.clicked = False

class TurretButton(Button):
    def __init__(self, spritesheet, atajo_teclado, x , y, single_click, tipo_torreta):
        super().__init__(spritesheet, atajo_teclado, x , y, single_click)
        self.turret_type = tipo_torreta

    def draw(self, surface, pressed_key):
        costo_torreta = e.torretas[self.turret_type][0]["precio"]

        if e.jugador["dinero"] < costo_torreta:
            surface.blit(self.images["blocked"], self.rect)
            return False
        
        return super().draw(surface, pressed_key)

class UpgradeButton(Button):
    def __init__(self, spritesheet, atajo_teclado, x, y, single_click):
        super().__init__(spritesheet, atajo_teclado, x, y, single_click)

    def draw(self, surface, pressed_key, selected_turret):
        if self.check_upgrade_available(selected_turret) == False:
            surface.blit(self.images["blocked"], self.rect)
            return False
        
        return super().draw(surface, pressed_key)
        
    def check_upgrade_available(self, selected_turret):
        if not(selected_turret.upgrade_level < 3):
            return False
        
        if not(e.jugador["dinero"] >= selected_turret.upgrade_cost):
            return False
        
        return True

# ------------------------------- #

# Carga de spritesheets y creación de los botones #

spritesheet_boton_tanque = Spritesheet("assets/imagenes/tienda/spritesheet_boton_tanque.png")
boton_tanque = TurretButton(spritesheet_boton_tanque, c.atajo_tanque, c.columna_tienda, c.pos_1, True, "Tanque")

spritesheet_boton_explosivos = Spritesheet("assets/imagenes/tienda/spritesheet_boton_explosivos.png")
boton_explosivos = TurretButton(spritesheet_boton_explosivos, c.atajo_explosivos, c.columna_tienda, c.pos_2, True, "Explosivos")

spritesheet_boton_comenzar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_comenzar.png")
boton_comenzar = Button(spritesheet_boton_comenzar, c.atajo_comenzar, c.columna_tienda, c.pos_5_a, True)

spritesheet_boton_mejorar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_mejorar.png")
boton_mejorar = UpgradeButton(spritesheet_boton_mejorar, c.atajo_mejorar, c.columna_tienda, c.pos_5, False)

spritesheet_boton_cancelar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_cancelar.png")
boton_cancelar = Button(spritesheet_boton_cancelar, c.atajo_cancelar_reembolso, c.columna_tienda, c.pos_6, True)

spritesheet_boton_reembolsar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_reembolsar.png")
boton_reembolsar = Button(spritesheet_boton_reembolsar, c.atajo_cancelar_reembolso, c.columna_tienda, c.pos_6, True)

# ------------------------------- #

# Que hacer a futuro #

# Hacer que todos las imagenes de los botones se encuentren en una solo spritesheet