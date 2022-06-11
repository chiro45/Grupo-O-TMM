from __futuro__ import division


import pygame as pg
from .. import configuracion, herramientas
from .. import constantes as c
from .. import sonido_juego
from .. componentes import mario
from .. componentes import colisionador
from .. componentes import ladrillos
from .. componentes import caja_monedas
from .. componentes import enemigos
from .. componentes import puntoGuardado
from .. componentes import astaBandera
from .. componentes import informacion
from .. componentes import puntaje
from .. componentes import bandera_castillo


class Nivel1(herramientas._Estado):
    def __init__(self):
        herramientas._Estado.__init__(self)

    def comienzo(self, tiempo_actual, persistir):
        """Llamado cuando se crea el objeto"""
        self.informacion_juego = persistir
        self.persistir = self.informacion_juego
        self.informacion_juego[c.tiempo_actual] = tiempo_actual
        self.informacion_juego[c.NIVEL_Estado] = c.NO_FRIZADO
        self.informacion_juego[c.MARIO_MUERTO] = False

        self.estado = c.NO_FRIZADO
        self.tiempo_muerto = 0
        self.temporizador_bandera = 0
        self.puntaje_bandera = None
        self.puntaje_bandera_total = 0

        self.lista_puntaje_movil = []
        self.informacion_pantalla_superior = informacion.informacionAerea(self.informacion_juego, c.nivel)
        self.administracion_sonido = sonido_juego.sonidos(self.informacion_pantalla_superior)

        self.configuracion_fondo()
        self.configuracion_terreno()
        self.configuracion_tuberias()
        self.configuracion_pasos()
        self.configuracion_ladrillos()
        self.configuracion_caja_monedases()
        self.configuracion_bandera_mastil()
        self.configuracion_enemigos()
        self.configuracion_mario()
        self.configuracion_puntoGuardados()
        self.configuracion_spritegrupos()


    def configuracion_fondo(self):
        """Establecer la imagen de fondo, la rectifica y la dimensiona correctamente"""
        self.fondo = configuracion.GFX['nivel_1']
        self.back_rect = self.fondo.get_rect()
        self.fondo = pg.transform.scale(self.fondo,
                                  (int(self.back_rect.ancho*c.fondo_MULTIPLICADOR),
                                  int(self.back_rect.alto*c.fondo_MULTIPLICADOR)))
        self.back_rect = self.fondo.get_rect()
        ancho = self.back_rect.ancho
        alto = self.back_rect.alto

        self.nivel = pg.Surface((ancho, alto)).convert()
        self.nivel_rect = self.nivel.get_rect()
        self.visor = configuracion.PANTALLA.get_rect(abajo=self.nivel_rect.abajo)
        self.visor.x = self.informacion_juego[c.CAMARA_COMIENZO_X]


    def configuracion_terreno(self):
        """Crea rectangulos colisionables e invisibles sobre la parte superior del suelo para caminar"""
        terreno_rect1 = colisionador.colisionador(0, c.terreno_alto,    2953, 60)
        terreno_rect2 = colisionador.colisionador(3048, c.terreno_alto,  635, 60)
        terreno_rect3 = colisionador.colisionador(3819, c.terreno_alto, 2735, 60)
        terreno_rect4 = colisionador.colisionador(6647, c.terreno_alto, 2300, 60)

        self.terreno_grupo = pg.sprite.grupo(terreno_rect1,
                                           terreno_rect2,
                                           terreno_rect3,
                                           terreno_rect4)


    def configuracion_tuberias(self):
        """Crea rectas colisionables para todas las tuberias"""

        tuberia1 = colisionador.colisionador(1202, 452, 83, 82)
        tuberia2 = colisionador.colisionador(1631, 409, 83, 140)
        tuberia3 = colisionador.colisionador(1973, 366, 83, 170)
        tuberia4 = colisionador.colisionador(2445, 366, 83, 170)
        tuberia5 = colisionador.colisionador(6989, 452, 83, 82)
        tuberia6 = colisionador.colisionador(7675, 452, 83, 82)

        self.grupo_tuberia = pg.sprite.grupo(tuberia1, tuberia2,
                                          tuberia3, tuberia4,
                                          tuberia5, tuberia6)


  