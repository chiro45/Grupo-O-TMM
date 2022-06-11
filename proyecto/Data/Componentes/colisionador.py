import pygame as pg
from .. import constantes as c

class Colisionador(pg.sprite.Sprite):
    """Sprites invisibles colocados sobre partes de fondo superiores
    que puedan ser colisionados (tuberías, escalones, suelo, etc.)"""
    def __init__(self, x, y, ancho, alto, nombre='colisionador'):
        pg.sprite.Sprite.__init__(self)
        self.imagen = pg.Surface((ancho, alto)).convert()
        #self.imagen.fill(c.RED)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estado = None