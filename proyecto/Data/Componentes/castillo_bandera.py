import pygame as pg
from .. import configuracion
from .. import constantes as c

class Bandera(pg.sprite.Sprite):
    """Bandera en el castillo"""
    def __init__(self, x, y):
        """Incia objeto"""
        super(Bandera, self).__init__()
        self.sprite_sheet = configuracion.GFX['item_objetos']
        self.imagen = self.get_imagen(129, 2, 14, 14)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estado = 'eleva'
        self.y_vel = -2
        self.altura_objetivo = y


    def get_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de la hoja de sprites."""
        imagen = pg.Superficie([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave(c.NEGRO)
        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_MULTIPLICADOR)))
        return imagen

    def update(self, *args):
        """Actualiza la posición de la bandera"""
        if self.estado == 'eleva':
            self.eleva()
        elif self.estado == 'descansa':
            self.descansa()

    def eleva(self):
        """Indica cuándo se iza la bandera para estar en el castillo"""
        self.rect.y += self.y_vel
        if self.rect.abajo <= self.altura_objetivo:
            self.estado = 'descansa'

    def descansa(self):
        """Estado de cuando la bandera está sin hacer nada"""
        pass
