
import pygame as pg
from .. import constantes as c


class puntoGuardado(pg.sprite.Sprite):
    """Sprite invisible usado para agregar enemigos, cajas especiales
    y gatillo deslizándose por el asta de la bandera"""
    def __init__(self, x, nombre, y=0, ancho=10, alto=600):
        super(puntoGuardado, self).__init__()
        self.imagen = pg.Surface((ancho, alto))
        self.imagen.fill(c.BLACK)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nombre = nombre