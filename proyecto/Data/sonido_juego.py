
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
        elif self.informacion_juego.state == c.JUEGO_TERMINADO:
            pg.mixer.music.load(self.diccionario_music['juego_terminado'])
            pg.mixer.music.play()
            self.estado = c.GAME_OVER


    def actualizar(self, informacion_juego , mario):
        "===========Actualiza el sonido con informacion del juego ==============="
        self.informacion_juego  = informacion_juego 
        self.mario = mario
        self.manejador_estado()

    def  manejador_estado(self):
        "==============Maneja el estado del sonido de los objetos==========="
        if self.estado == c.NORMAL:
            if self.mario.muere:
                self.inicia_musica('muerte', c.MARIO_MUERTO)
            elif self.mario.invencible \
                    and self.mario.pierde_invencibilidad == False:
                self.inicia_musica('invencible', c.MARIO_INVENCIBLE)
            elif self.mario == c.ASTA_DE_BANDERA:
                self.inicia_musica('bandera1', c.ASTA_DE_BANDERA)
            elif self.informacion_juego.tiempo == 100:
                self.inicia_musica('poco_tiempo', c.AVISO_DE_TIEMPO)


        elif self.estado == c.ASTA_DE_BANDERA:
            if self.mario.estado == c.CAMINANDO_AL_CASTILLO:
                self.inicia_musica('nivel_terminado', c.NIVEL_TERMINADO)

        elif self.estado == c.NIVEL_TERMINADO:
            if self.mario.en_castillo:
                self.inicia_musica['cuenta_atras_monedas'].play()
                self.estado = c.CUENTA_REGRESIVA_RAPIDA

       
