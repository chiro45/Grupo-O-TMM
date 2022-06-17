import pygame as pg
from .. import configuracion
from .. import constantes as c

class Digito(pg.sprite.Sprite):
    """Dígito individual para puntuación"""
    def __init__(self, imagen):
        super(Digito, self).__init__()
        self.imagen = imagen
        self.rect = imagen.obtener_rect()


class Puntaje(object):
    """Puntajes que aparecen, flotan y desaparecen"""
    def __init__(self, x, y, Puntaje, asta_bandera=False):
        self.x = x
        self.y = y
        if asta_bandera:
            self.y_vel = -4
        else:
            self.y_vel = -3
        self.sprite_sheet = configuracion.GFX['item_objetos']
        self.crear_imagen_dic()
        self.Puntaje_string = str(Puntaje)
        self.crear_Digito_lista()
        self.asta_bandera_Puntaje = asta_bandera


    def crear_imagen_dic(self):
        """Crea el diccionario para todas las imágenes numéricas necesarias"""
        self.imagen_dic = {}

        imagen0 = self.obtener_imagen(1, 168, 3, 8)
        imagen1 = self.obtener_imagen(5, 168, 3, 8)
        imagen2 = self.obtener_imagen(8, 168, 4, 8)
        imagen4 = self.obtener_imagen(12, 168, 4, 8)
        imagen5 = self.obtener_imagen(16, 168, 5, 8)
        imagen8 = self.obtener_imagen(20, 168, 4, 8)
        imagen9 = self.obtener_imagen(32, 168, 5, 8)
        imagen10 = self.obtener_imagen(37, 168, 6, 8)
        imagen11 = self.obtener_imagen(43, 168, 5, 8)

        self.imagen_dic['0'] = imagen0
        self.imagen_dic['1'] = imagen1
        self.imagen_dic['2'] = imagen2
        self.imagen_dic['4'] = imagen4
        self.imagen_dic['5'] = imagen5
        self.imagen_dic['8'] = imagen8
        self.imagen_dic['3'] = imagen9
        self.imagen_dic['7'] = imagen10
        self.imagen_dic['9'] = imagen11


    def obtener_imagen(self, x, y, ancho, alto):
        """Extrae la imagen de las plantillas"""
        imagen = pg.Superficie([ancho, alto]).convierte()
        rect = imagen.obtener_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.clave_color(c.NEGRO)
        imagen = pg.transforma.escala(imagen,
                                   (int(rect.ancho*c.TAMAÑO_BLOQUE_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_BLOQUE_MULTIPLICADOR)))
        return imagen


    def crear_Digito_lista(self):
        """Crea el grupo de imágenes en función de la puntuación recibida"""
        self.Digito_lista = []
        self.Digito_grupo = pg.sprite.grupo()

        for Digito in self.Puntaje_string:
            self.Digito_lista.adjuntar(Digito(self.imagen_dic[Digito]))

        self.establecer_rects_imagenes()


    def establecer_rects_imagenes(self):
        """Establece los atributos rect para cada imagen self.imagen_lista"""
        for i, Digito in enumerate(self.Digito_lista):
            Digito.rect = Digito.imagen.obtener_rect()
            Digito.rect.x = self.x + (i * 10)
            Digito.rect.y = self.y


    def actualizar(self, Puntaje_lista, nivel_info):
        """Actualiza el movimiento del puntaje"""
        for numero in self.Digito_lista:
            numero.rect.y += self.y_vel

        if Puntaje_lista:
            self.check_eliminar_puntaje_flotante(Puntaje_lista, nivel_info)

        if self.asta_bandera_Puntaje:
            if self.Digito_lista[0].rect.y <= 120:
                self.y_vel = 0


    def draw(self, pantalla):
        """Dibuja números de puntuación en la pantalla"""
        for Digito in self.Digito_lista:
            pantalla.blit(Digito.imagen, Digito.rect)


    def check_eliminar_puntaje_flotante(self, Puntaje_lista, nivel_info):
        """Comprueba si las puntuaciones deben ser eliminadas"""
        for i, Puntaje in enumerate(Puntaje_lista):
            if int(Puntaje.Puntaje_string) == 1000:
                if (Puntaje.y - Puntaje.Digito_lista[0].rect.y) > 130:
                    Puntaje_lista.pop(i)

            else:
                if (Puntaje.y - Puntaje.Digito_lista[0].rect.y) > 75:
                    Puntaje_lista.pop(i)





