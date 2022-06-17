import pygame as pg
from .. import configuracion
from .. import constantes as c

class Bandera(pg.sprite.Sprite):
    """Bandera en la parte superior del asta al final del nivel"""
    def __init__(self, x, y):
        super(Bandera, self).__init__()
        self.sprite_sheet = configuracion.GFX['item_objetos']
        self.config_imagenes()
        self.imagen = self.frames[0]
        self.rect = self.imagen.get_rect()
        self.rect.derecha = x
        self.rect.y = y
        self.estado = c.ARRIBA_MASTIL
   
    def config_imagenes(self):
        """Configura una lista de frames"""
        self.frames = []

        self.frames.adjuntar(
            self.obtener_imagen(128, 32, 16, 16))


    def obtener_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de las plantillas"""
        imagen = pg.Superficie([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave_color(c.NEGRO)
        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_BLOQUE_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_BLOQUE_MULTIPLICADOR)))
        return imagen


    def actualizar(self, *args):
        """Actualiza el comportamiento"""
        self.manejar_estado()


    def manejar_estado(self):
        """Determina el comportamiento basado en el estado"""
        if self.estado == c.ARRIBA_MASTIL:
            self.imagen = self.frames[0]
        elif self.estado == c.MEDIO_MASTIL:
            self.deslizandose()
        elif self.estado == c.BAJO_MASTIL:
            self.imagen = self.frames[0]


    def deslizandose(self):
        """Estado cuando Mario llega al asta de la bandera"""
        self.y_vel = 5
        self.rect.y += self.y_vel

        if self.rect.abajo >= 485:
            self.estado = c.BAJO_MASTIL


class Asta(pg.sprite.Sprite):
    """Asta sobre la que está la bandera"""
    def __init__(self, x, y):
        super(Asta, self).__init__()
        self.sprite_sheet = configuracion.GFX['tile_set']
        self.configuracion_frames()
        self.imagen = self.frames[0]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y


    def configuracion_frames(self):
        """Crear la lista de frames"""
        self.frames = []

        self.frames.adjuntar(
            self.obtener_imagen(263, 144, 2, 16))


    def obtener_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de las plantillas"""
        imagen = pg.Superficie([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave_color(c.NEGRO)
        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_BLOQUE_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_BLOQUE_MULTIPLICADOR)))
        return imagen


    def actualizar(self, *args):
        """Marcador de posición para actualizar, ya que no hay nada que actualizar"""
        pass


class Final(pg.sprite.Sprite):
    """La parte superior del asta de la bandera"""
    def __init__(self, x, y):
        super(Final, self).__init__()
        self.sprite_sheet = configuracion.GFX['tile_set']
        self.configuracion_frames()
        self.imagen = self.frames[0]
        self.rect = self.imagen.get_rect()
        self.rect.centrox = x
        self.rect.abajo = y


    def configuracion_frames(self):
        """Crea la lista de frames propios"""
        self.frames = []

        self.frames.adjuntar(
            self.obtener_imagen(228, 120, 8, 8))


    def obtener_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de las plantillas"""
        imagen = pg.Superficie([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave_color(c.NEGRO)
        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_MULTIPLICADOR)))
        return imagen


    def actualizar(self, *args):
        pass



