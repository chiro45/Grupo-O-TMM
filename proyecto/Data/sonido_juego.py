
import pygame as pg
from . import setup
from . import constantes as c

class Sonido(object):
    "===========Manjejador de eventos de todos los sonidos del juego==========="
    def __init__(self, informarcion_general):
        "===========Inicializamos las clases==========="
        self.diccionario_fx= setup.SFX
        self.diccionario_music = setup.MUSIC
        self.informarcion_general= informarcion_general
        self.informacion_juego = informarcion_general.info_juego
        self.configuracion_mezclador_musica()



    def configuracion_mezclador_musica(self):
        "==========Setea la musica por el nivel================"
        if self.informarcion_general.estado == c.NIVEL:
            pg.mixer.music.load(self.diccionario_music['tema_base'])
            pg.mixer.music.play()
            self.estado = c.NORMAL
        elif self.overhead_info.state == c.JUEGO_TERMINADO:
            pg.mixer.music.load(self.diccionario_music['juego_terminado'])
            pg.mixer.music.play()
            self.estado = c.GAME_OVER


    def actualizar(self, informacion_juego , mario):
        "===========Actualiza el sonido con informacion del juego ==============="
        self.informacion_juego  = informacion_juego 
        self.mario = mario
        self.manejador_estado()

   


