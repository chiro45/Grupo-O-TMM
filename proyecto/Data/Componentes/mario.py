

import pygame as pg
from .import constantes as c
from .. import configuracion, herramientas


class Mario(pg.sprite.Sprite):
    #contructor de la clase mario
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = configuracion.GFX['mario_bros']
        self.configuracion_Tiempo()
        self.configuracion_estados_booleanos()
        self.configuracion_fuerzas()
        self.configuracion_contadores()
        self.carga_imagenes_desde_plantillas()

        

    
    def configuracion_Tiempo(self):
        """Sets up timers for animations"""
        self.temporizador_caminando = 0
        self.temporizador_invencible_animation = 0
        self.inicio_temportizador_invencible_animation = 0
        self.temporizador_transicion_fuego = 0
        self.temporizador_muerte = 0
        self.temporizador_transicion = 0
        self.ultimo_tiempo_bolaDeFuego = 0
        self.temporizador_herida_invisible = 0
        self.temporizador_herida_invisible2 = 0
        self.tiempo_del_asta_bandera = 0


   
        


    
        