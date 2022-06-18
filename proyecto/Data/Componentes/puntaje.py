import pygame as pg
from .. import configuracion
from .. import constantes as c

class Digito(pg.sprite.Sprite):
    """Dígito individual para puntuación"""
    def __init__(self, image):
        super(Digito, self).__init__()
        self.image = image
        self.rect = image.obtener_rect()


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
        self.crear_image_dic()
        self.Puntaje_string = str(Puntaje)
        self.crear_Digito_lista()
        self.asta_bandera_Puntaje = asta_bandera


    def crear_image_dic(self):
        """Crea el diccionario para todas las imágenes numéricas necesarias"""
        self.image_dic = {}

        image0 = self.obtener_image(1, 168, 3, 8)
        image1 = self.obtener_image(5, 168, 3, 8)
        image2 = self.obtener_image(8, 168, 4, 8)
        image4 = self.obtener_image(12, 168, 4, 8)
        image5 = self.obtener_image(16, 168, 5, 8)
        image8 = self.obtener_image(20, 168, 4, 8)
        image9 = self.obtener_image(32, 168, 5, 8)
        image10 = self.obtener_image(37, 168, 6, 8)
        image11 = self.obtener_image(43, 168, 5, 8)

        self.image_dic['0'] = image0
        self.image_dic['1'] = image1
        self.image_dic['2'] = image2
        self.image_dic['4'] = image4
        self.image_dic['5'] = image5
        self.image_dic['8'] = image8
        self.image_dic['3'] = image9
        self.image_dic['7'] = image10
        self.image_dic['9'] = image11


    def obtener_image(self, x, y, ancho, alto):
        """Extrae la image de las plantillas"""
        image = pg.Superficie([ancho, alto]).convierte()
        rect = image.obtener_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        image.set_colorkey(c.NEGRO)
        image = pg.transform.scale(image,
                                   (int(rect.ancho*c.TAMAÑO_BLOQUE_MULTIPLICADOR),
                                    int(rect.alto*c.TAMAÑO_BLOQUE_MULTIPLICADOR)))
        return image


    def crear_Digito_lista(self):
        """Crea el grupo de imágenes en función de la puntuación recibida"""
        self.Digito_lista = []
        self.Digito_grupo = pg.sprite.grupo()

        for Digito in self.Puntaje_string:
            self.Digito_lista.adjuntar(Digito(self.image_dic[Digito]))

        self.establecer_rects_imagees()


    def establecer_rects_imagees(self):
        """Establece los atributos rect para cada image self.image_lista"""
        for i, Digito in enumerate(self.Digito_lista):
            Digito.rect = Digito.image.obtener_rect()
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
            pantalla.blit(Digito.image, Digito.rect)


    def check_eliminar_puntaje_flotante(self, Puntaje_lista, nivel_info):
        """Comprueba si las puntuaciones deben ser eliminadas"""
        for i, Puntaje in enumerate(Puntaje_lista):
            if int(Puntaje.Puntaje_string) == 1000:
                if (Puntaje.y - Puntaje.Digito_lista[0].rect.y) > 130:
                    Puntaje_lista.pop(i)

            else:
                if (Puntaje.y - Puntaje.Digito_lista[0].rect.y) > 75:
                    Puntaje_lista.pop(i)





