from config import pg
from spritesheet import Spritesheet

import config as c
import estadisticas as e

class Boton(pg.sprite.Sprite):
    def __init__(self, spritesheet, spritesheet_column, x , y, single_click):
        pg.sprite.Sprite.__init__(self)

        self.images = {
            "normal": 0,
            "hover": 52,
            "blocked": 104,
        }

        for image in self.images:
            self.images[image] = spritesheet.obtener_imagen(c.ancho_boton_tienda, c.alto_boton_tienda, spritesheet_column, self.images[image])

        # ------------------------------- #

        self.rect = self.images["normal"].get_rect()
        self.rect.topleft = (x, y)
        self.delay = 100
        self.clicked = False
        self.last_clicked = 0
        self.single_click = single_click
    
    def dibujar(self, surface):
        posicion_mouse = pg.mouse.get_pos()
        tiempo_actual = pg.time.get_ticks()
        accion = False

        if not (self.rect.collidepoint(posicion_mouse)):
            surface.blit(self.images["normal"], self.rect)
            return accion
        
        surface.blit(self.images["hover"], self.rect)
        
        if ((pg.mouse.get_pressed()[0] == 1 and self.clicked == False and tiempo_actual - self.last_clicked >= self.delay)):
            self.last_clicked = tiempo_actual
            accion = True

            if self.single_click:
                self.clicked = True
                
            return accion

        self.clicked = False

class BotonTorreta(Boton):
    def __init__(self, spritesheet, spritesheet_column, x, y, single_click, tipo_torreta):
        super().__init__(spritesheet, spritesheet_column, x, y, single_click)
        self.turret_type = tipo_torreta

    def dibujar(self, surface):
        costo_torreta = e.torretas[self.turret_type][0]["precio"]

        if e.jugador["dinero"] < costo_torreta:
            surface.blit(self.images["blocked"], self.rect)
            return False
        
        return super().dibujar(surface)

class VelocidadBoton(Boton):
    def __init__(self, spritesheet, spritesheet_column, x, y, single_click):
        super().__init__(spritesheet, spritesheet_column, x, y, single_click)

    def dibujar(self, surface):
        posicion_mouse = pg.mouse.get_pos()
        tiempo_actual = pg.time.get_ticks()
        accion = False

        if not(self.rect.collidepoint(posicion_mouse)):
            if self.clicked:
                image = self.images["blocked"]
            else:
                image = self.images["normal"]

            surface.blit(image, self.rect)
            return accion
        
        surface.blit(self.images["hover"], self.rect)

        if pg.mouse.get_pressed()[0] == 1 and tiempo_actual - self.last_clicked >= self.delay:
            self.last_clicked = tiempo_actual
            self.clicked = not(self.clicked)
            accion = True
  
            return accion


class MejorarBoton(Boton):
    def __init__(self, spritesheet, spritesheet_column, x, y, single_click):
        super().__init__(spritesheet, spritesheet_column, x, y, single_click)

    def dibujar(self, surface, selected_turret):
        if self.check_upgrade_available(selected_turret) == False:
            surface.blit(self.images["blocked"], self.rect)
            return False
        
        return super().dibujar(surface)
        
    def check_upgrade_available(self, selected_turret):
        if not(selected_turret.upgrade_level < 3):
            return False
        
        if not(e.jugador["dinero"] >= selected_turret.upgrade_cost):
            return False
        
        return True
    
class MenuBoton(Boton):
    def __init__(self, spritesheet, spritesheet_column, lenght, height, x, y, single_click):
        super().__init__(spritesheet, spritesheet_column, x, y, single_click)

        self.images = {
            "normal": 0,
            "hover": 83,
        }

        for image in self.images:
            self.images[image] = spritesheet.obtener_imagen(lenght, height, spritesheet_column, self.images[image])

        self.rect = self.images["normal"].get_rect()
        self.rect.topleft = (x, y)

    def dibujar(self, surface):
        return super().dibujar(surface)

# ------------------------------- #

# Carga de spritesheets y creación de los botones #

spritesheet_botones_menu = Spritesheet("assets/imagenes/menu/spritesheet_botones_menu0.png")

boton_jugar = MenuBoton(spritesheet_botones_menu, c.columna_boton_jugar, c.ancho_boton_jugar, c.alto_boton_jugar, 306, 420, True)
boton_salir = MenuBoton(spritesheet_botones_menu, c.columna_boton_salir, c.ancho_boton_salir, c.alto_boton_salir, 370, 520, True)
boton_reintentar = MenuBoton(spritesheet_botones_menu, c.columna_boton_reintentar, c.ancho_boton_reintentar, c.alto_boton_reintertar, 352, 420, True)

spritesheet_botones_tienda = Spritesheet("assets/imagenes/tienda/spritesheet_botones_tienda.png")

boton_tanque = BotonTorreta(spritesheet_botones_tienda, c.columna_boton_tanque, c.columna_tienda, c.pos_1, True, "Tanque")
boton_velocidad = VelocidadBoton(spritesheet_botones_tienda, c.columna_boton_velocidad, c.columna_tienda, c.pos_2, True)
boton_comenzar = Boton(spritesheet_botones_tienda, c.columna_boton_comenzar, c.columna_tienda, c.pos_3, True)
boton_mejorar = MejorarBoton(spritesheet_botones_tienda, c.columna_boton_mejorar, c.columna_tienda, c.pos_5, True)
boton_cancelar = Boton(spritesheet_botones_tienda, c.columna_boton_cancelar, c.columna_tienda, c.pos_6, True)
boton_reembolsar = Boton(spritesheet_botones_tienda, c.columna_boton_reembolsar, c.columna_tienda, c.pos_6, True)