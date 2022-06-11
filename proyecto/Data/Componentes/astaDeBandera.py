import pygame as pg
from .. import configuracion
from .. import constantes as c

class Bandera(pg.sprite.Sprite):
    """Bandera en la parte superior del asta al final del nivel"""
    def __init__(self, x, y):
        super(Bandera, self).__init__()
        self.sprite_sheet = configuracion.GFX['item_objects']
        self.config_imagenes()
        self.imagen = self.frames[0]
        self.rect = self.imagen.get_rect()
        self.rect.derecha = x
        self.rect.y = y
        self.estado = c.ARRIBA_MASTIL