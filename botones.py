from spritesheet import Spritesheet

import config as c
import pygame as pg
import estadisticas as e
import texto as text

class Button(pg.sprite.Sprite):
    def __init__(self, spritesheet, x , y, single_click):
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
        self.rect = self.images["normal"].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click
    
    def draw(self, surface):
        posicion_mouse = pg.mouse.get_pos()
        accion = False
        
        if not(self.rect.collidepoint(posicion_mouse)):
            surface.blit(self.images["normal"], self.rect)
            return accion
        
        surface.blit(self.images["hover"], self.rect)
        
        if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            accion = True

            if self.single_click:
                self.clicked = True
                #print("clicked")

            return accion

        self.clicked = False

class TurretButton(Button):
    def __init__(self, spritesheet, x , y, single_click, tipo_torreta):
        super().__init__(spritesheet, x , y, single_click)
        self.turret_type = tipo_torreta

    def draw(self, surface):
        costo_torreta = e.torretas[self.turret_type][0]["precio"]

        if self.rect.collidepoint(pg.mouse.get_pos()):
                text.draw_text(str(costo_torreta), text.text_font, "grey100", 780, 142)

        if e.jugador["dinero"] < costo_torreta:
            surface.blit(self.images["blocked"], self.rect)
            return False
         
        return super().draw(surface)

class UpgradeButton(Button):
    def __init__(self, spritesheet, x, y, single_click):
        super().__init__(spritesheet, x , y, single_click)

    def draw(self, surface, selected_turret):
        if self.rect.collidepoint(pg.mouse.get_pos()):
                if selected_turret.upgrade_cost <= 0:
                    message = "MAX"
                else:
                    message = str(selected_turret.upgrade_cost)

                text.draw_text(message, text.text_font, "grey100", 780, 142)

        if self.check_upgrade_available(selected_turret) == False:
            surface.blit(self.images["blocked"], self.rect)
            return False
        
        return super().draw(surface)
        
    def check_upgrade_available(self, selected_turret):
        if not(selected_turret.upgrade_level < 3):
            return False
        
        if not(e.jugador["dinero"] >= selected_turret.upgrade_cost):
            return False
        
        return True

class BeginButton(Button):
    def __init__(self, spritesheet, x, y, single_click):
        super().__init__(spritesheet, x, y, single_click)

    def draw(self, surface, pressed_key):
        if c.level_started == True:
            surface.blit(self.images["blocked"], self.rect)

        else:
            return super().draw(surface)

# ------------------------------- #

# Carga de spritesheets y creación de los botones #

spritesheet_boton_tanque = Spritesheet("assets/imagenes/tienda/spritesheet_boton_tanque.png")
boton_tanque = TurretButton(spritesheet_boton_tanque, c.columna_tienda, c.pos_1, True, "Tanque")

spritesheet_boton_explosivos = Spritesheet("assets/imagenes/tienda/spritesheet_boton_explosivos.png")
boton_explosivos = TurretButton(spritesheet_boton_explosivos, c.columna_tienda, c.pos_2, True, "Explosivos")

spritesheet_boton_comenzar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_comenzar.png")
boton_comenzar = BeginButton(spritesheet_boton_comenzar, c.columna_tienda, c.pos_2, True)

spritesheet_boton_mejorar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_mejorar.png")
boton_mejorar = UpgradeButton(spritesheet_boton_mejorar, c.columna_tienda, c.pos_5, False)

spritesheet_boton_cancelar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_cancelar.png")
boton_cancelar = Button(spritesheet_boton_cancelar, c.columna_tienda, c.pos_6, True)

spritesheet_boton_reembolsar = Spritesheet("assets/imagenes/tienda/spritesheet_boton_reembolsar.png")
boton_reembolsar = Button(spritesheet_boton_reembolsar, c.columna_tienda, c.pos_6, True)

# ------------------------------- #

# Que hacer a futuro #

# Hacer que todos las imagenes de los botones se encuentren en una solo spritesheet

# ------------------------------- #