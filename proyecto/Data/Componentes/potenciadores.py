import pygame as pg
from .. import constantes as c
from .. import configuracion


class Potenciar(pg.sprite.Sprite):
    """Clase base"""
    def __init__(self, x, y):
        super(Potenciar, self).__init__()


    def configuracion_Potenciar(self, x, y, nombre, configuracion_frames):
        
        self.sprite_sheet = configuracion.GFX['item_objetos']
        self.frames = []
        self.frame_index = 0
        configuracion_frames()
        self.imagen = self.frames[self.frame_index]
        self.rect = self.imagen.obtener_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.estado = c.REVELADO
        self.y_vel = -1
        self.x_vel = 0
        self.direccion = c.DERECHA
        self.box_alto = y
        self.gravedad = 1
        self.max_y_vel = 8
        self.animar_temp = 0
        self.nombre = nombre


    def obtener_imagen(self, x, y, ancho, alto):
        """Obtener los marcos de imagen de plantillas"""

        imagen = pg.Superficie([ancho, alto]).convertir()
        rect = imagen.obtener_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave_color(c.NEGRO)


        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_MULTIPLICADOR)))
        return imagen


    def actualizar(self, juego_info, *args):
        """Actualiza el comportamiento de encendido"""
        self.tiempo_actual = juego_info[c.tiempo_actual]
        self.manejar_estado()


    def manejar_estado(self):
        pass


    def REVELADOing(self, *args):
        """Acción cuando el encendido deja la caja de monedas o el ladrillo."""
        self.rect.y += self.y_vel

        if self.rect.abajo <= self.box_alto:
            self.rect.abajo = self.box_alto
            self.y_vel = 0
            self.estado = c.DESLIZANDOSE


    def deslizarse(self):
        """Acción para cuando el encendido se desliza por el suelo"""
        if self.direccion == c.DERECHA:
            self.x_vel = 3
        else:
            self.x_vel = -3


    def cayendo(self):
        """Cuando los potenciadores caen de una repisa"""
        if self.y_vel < self.max_y_vel:
            self.y_vel += self.gravedad


