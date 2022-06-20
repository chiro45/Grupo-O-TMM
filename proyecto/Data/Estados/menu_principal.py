"""ponemos la configuracion del menu principal"""

import pygame as pg
from .. import configuracion, herramientas
from .. import constantes as c
from .. Componentes import info, mario


class Menu(herramientas._State):
    def __init__(self):
        """Inicializa el estado"""
        herramientas._State.__init__(self)
        persistir = {
                   c.TOTAL_MONEDAS: 0,
                   c.PUNTAJE: 0,
                   c.VIDAS: 3,
                   c.MEJOR_PUNTAJE: 0,
                   c.TIEMPO_ACTUAL: 0.0,
                   c.ESTADO_DEL_NIVEL: None,
                   c.COMIENZO_CAMARA_X: 0,
                   c.MARIO_MUERTO: False}
        self.comienzo(0.0, persistir)

    def comienzo(self, tiempo_actual, persistir):
        """ Hace el llamado cada vez que el juego cambia de estado, e inicializa ciertos valores"""
        self.siguiente = c.PANTALLA_DE_CARGA
        self.persistir = persistir
        self.info_del_juego = persistir
        self.informacion_general = info.InformacionGeneral(self.info_del_juego, c.MENU_PRINCIPAL)

        self.sprite_sheet = configuracion.GFX['title_screen']
        self.configuracion_fondo()
        self.configuracion_mario()
        self.configuracion_cursor()


    def configuracion_cursor(self):
        """Crea el cursor de un honguito en la pantalla principal para seleccionar 1 o 2 jugadores"""
        self.cursor = pg.sprite.Sprite()
        dest = (220, 358)
        self.cursor.imagen, self.cursor.rect = self.get_imagen(
            24, 160, 8, 8, dest, configuracion.GFX['item_objects'])
        self.cursor.estado = c.PLAYER1


    def configuracion_mario(self):
        """Coloca a mario en el principio del nivel 1"""
        self.mario = mario.Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.ALTURA_SUELO


    def configuracion_fondo(self):
        """Configura la imagen de fondo para blit"""
        self.fondo = configuracion.GFX['nivel_1']
        self.background_rect = self.fondo.get_rect()
        self.fondo = pg.transform.scale(self.fondo,
                                   (int(self.background_rect.ancho*c.MULTIPLICADOR_FONDO),
                                    int(self.background_rect.alto*c.MULTIPLICADOR_FONDO)))
        self.visor = configuracion.PANTALLA.get_rect(bottom=configuracion.PANTALLA_RECT.bottom)

        self.image_dict = {}
        self.image_dict['NOMBRE_CAJA_JUEGO'] = self.get_imagen(
            1, 60, 176, 88, (170, 100), configuracion.GFX['titulo_pantalla'])


def obtener_imagen(self, x, y, ancho, alto, dest, sprite_sheet):
        "===========RETORNA LA IMAGEN QUE SE VERA EN PANTALLA Y LA ACTUALIZA"
        imagen = pg.Surface([ancho, alto])
        tamano_rectangulo = imagen.get_rect()

        imagen.blit(sprite_sheet, (0, 0), (x, y, ancho, alto))

        if sprite_sheet == configuracion.GFX['titulo_pantalla']:
            imagen.set_colorkey((255, 0, 220))
            imagen = pg.transform.scale(imagen,
                                   (int(tamano_rectangulo.width* c.TAMAÑO_MULTIPLICADOR),
                                    int(tamano_rectangulo.height*  c.TAMAÑO_MULTIPLICADOR)))
        else:
            imagen.set_colorkey(c.NEGRO)
            imagen = pg.transform.scale(imagen,
                                   (int(tamano_rectangulo.width * 3),
                                    int(tamano_rectangulo.height * 3)))

        tamano_rectangulo = imagen.get_rect()
        tamano_rectangulo.x = dest[0]
        tamano_rectangulo.y = dest[1]
        return (imagen, tamano_rectangulo)


def actualizar(self, superficie, teclas , tiempo_actual):
             "============ACTUALIZA LOS CAMBIOS DEL ESTADO EN TODO MOMENTO========="
             
             self.tiempo_actual = tiempo_actual
             self.informacion_juego[c.TIEMPO_ACTUAL] = self.tiempo_actual
             self.actualizarCurso(teclas)
             self.informacionGeneral.actualizar(self.informacion_juego)

             superficie.blit(self.fondo, self.visor, self.visor)
             superficie.blit(self.image_dict['NOMBRE_CAJA_JUEGO'][0],self.image_dict['NOMBRE_CAJA_JUEGO'][1])
             superficie.blit(self.mario.imagen, self.mario.rect)
             superficie.blit(self.cursor.imagen, self.cursor.rect)
             self.informacionGeneral.dibujar(superficie)


def actualizarCurso(self, teclas):
        "========================================ACTUALIZA EL CURSOR AL SELECCIONAR==============="
        lista_entradas = [pg.K_RETURN, pg.K_a, pg.K_s]

        if self.cursor.estado == c.PLAYER1:
            self.cursor.rect.y = 358
            if teclas[pg.K_DOWN]:
                self.cursor.estatado = c.PLAYER2
            for input in lista_entradas:
                if teclas[input]:
                    self.resetear_informacion_juego()
                    self.hecho = True
        elif self.cursor.estado == c.PLAYER2:
            self.cursor.rect.y = 403
            if teclas[pg.K_UP]:
                self.cursor.estado = c.PLAYER1


def resetear_informacion_juego(self):
        "===============RESETEA TODO AL PERDER EL JUEGO============================="
        self.informacion_juego[c.TOTAL_MONEDAS] = 0
        self.informacion_juego[c.PUNTAJE] = 0
        self.informacion_juego[c.VIDAS] = 3
        self.informacion_juego[c.TIEMPO_ACTUAL] = 0.0
        self.informacion_juego[c.ESTADO_DEL_NIVEL] = None

        self.persistir = self.informacion_juego