"""ponemos la configuracion del menu principal"""

import pygame as pg
from .. import configuracion, herramientas
from .. import constants as c
from .. Componentes import info, mario


class Menu(herramientas._State):
    def __init__(self):
        """Inicializa el estado"""
        herramientas._State.__init__(self)
        persistir = {c.TOTAL_MONEDAS: 0,
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