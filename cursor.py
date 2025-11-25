from config import pg
from spritesheet import Spritesheet

import config as c
import manager as m

class Cursor():
    def __init__(self, spritesheet):
        pg.sprite.Sprite.__init__(self)
        pg.mouse.set_visible(False)

        self.images = {
            "normal": 0,
            "hover": 36,
        }

        for image in self.images:
            self.images[image] = spritesheet.obtener_imagen(c.ancho_cursor, c.alto_cursor, 0, self.images[image])

        self.rect = self.images["normal"].get_rect()

    def draw(self, surface):
        posicion_mouse = pg.mouse.get_pos()
        imagen = self.images["normal"]
        
        if m.creando_torretas:
            imagen = self.images["hover"]
            
        surface.blit(imagen, (posicion_mouse[0] - c.ancho_cursor // 2, posicion_mouse[1] - c.alto_cursor // 8))

spritesheet_cursor = Spritesheet("assets/imagenes/spritesheet_cursor.png")
cursor = Cursor(spritesheet_cursor)