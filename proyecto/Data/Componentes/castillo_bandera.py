import pygame as pg
from .. import configuracion
from .. import constantes as c

class Bandera(pg.sprite.Sprite):
    """Bandera en el castillo"""
    def __init__(self, x, y):
        """Incia objeto"""
        super(Bandera, self).__init__()
        self.sprite_sheet = configuracion.GFX['item_objects']
        self.imagen = self.get_imagen(129, 2, 14, 14)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estado = 'resting'
        self.y_vel = -2
        self.altura_objetivo = y


    def get_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de la hoja de sprites."""
        imagen = pg.Surface([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.set_colorkey(c.NEGRO)
        imagen = pg.transform.scale(imagen,
                                   (int(rect.ancho*c.TAMAÑO_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_MULTIPLICADOR)))
        return imagen

    def update(self, *args):
        """Actualiza la posición de la bandera"""
        if self.estado == 'resting':
            self.resting()
        elif self.estado == 'descansa':
            self.descansa()

    def resting(self):
        """Indica cuándo se iza la bandera para estar en el castillo"""
        self.rect.y += self.y_vel
        if self.rect.bottom <= self.altura_objetivo:
            self.estado = 'descansa'

    def descansa(self):
        """Estado de cuando la bandera está sin hacer nada"""
        pass
