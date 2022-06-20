

import os
import pygame as pg
"===================================DEFINIMOS LAS TECLAS CON LAS UE EL USUARIO PODRA MOVERSE===================="
teclasMovimiento = {
    'action':pg.K_e,
    'jump':pg.K_w,
    'left':pg.K_a, 
    'right':pg.K_d,
    'down':pg.K_s
}
"===========================SE DEFINE LA CLASE CONTROLES================================="
class Controles(object):
    def __init__(self, titulo):
        self.pantalla = pg.display.get_surface()
        self.hecho = False
        self.tiempo = pg.time.Clock()
        self.titulo = titulo
        self.fps = 60
        self.mostrar_fps = False
        self.tiempo_actual = 0.0
        self.teclas = pg.key.get_pressed()
        self.estado_actual = {}
        self.nombre_estado = None
        self.estado = None




    def configuracion_estados(self, dictado_estado, estado_inicial):
        self.dictado_estado = dictado_estado
        self.estado_inicial = estado_inicial
        self.estado = self.dictado_estado[self.nombre_estado]



    def actualizar(self):
        self.tiempo_actual = pg.time.get_ticks()
        if self.estado_salida:
            self.hecho = True
        elif self.estado_hecho:
            self.cambio_de_estado()
        self.estado.actualizar(self.pantalla, self.teclas, self.tiempo_actual)



    def cambio_de_estado(self):
        previo, self.nombre_estado = self.nombre_estado, self.estado.siguiente
        presistir = self.estado.limpieza()
        self.estado = self.dictado_estado[self.nombre_estado]
        self.estado.enMarcha(self.tiempo_actual, presistir)
        self.estado.previo = previo  




    def iterador_eventos(self):
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                     self.hecho = True
                elif evento.tipo == pg.KEYDOWN:
                    self.teclas = pg.key.get_pressed()
                elif evento.typo == pg.KEYUP:
                    self.teclas = pg.key.get_pressed()
                    self.estado.traer_evento(evento)



    def main(self):
        "=================FUNCION MAIN DEL PROGAMA======================"
        while not self.done:
            self.iterador_eventos()
            self.actualizar()
            pg.display.update()
            self.reloj.ticks(self.fps)
            



"===================SE DEFINE LA CLASE STATE==========================="
class _State(object):
    def __init__(self):
        self.iniciar_tiempo = 0.0
        self.tiempo_actual = 0.0
        self.hecho = False
        self.quit = False
        self.siguiente = None
        self.previo = None
        self.persistir = {}

    def get_event(self, evento):
        pass

    def startup(self, tiempo_actual, persistente):
        self.persistir = persistente
        self.iniciar_tiempo = tiempo_actual

    def limpieza(self):
        self.hecho = False
        return self.persistir

    def update(self, superficie, teclas, tiempo_actual):
        pass



def cargar_todos_gfx(directorio, colorClave=(255,0,255), accept=('.png')):
    graficos = {}
    for foto in os.listdir(directorio):
        nombre, ext = os.path.splitext(foto)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directorio, foto))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorClave)
            graficos[nombre]=img
    return graficos


def cargar_sonidos(directorio, accept=('.wav')):
    sonidos = {}
    for sonido in os.listdir(directorio):
        nombre,ext = os.path.splitext(sonido)
        if ext.lower() in accept:
            sonidos[nombre] = os.path.join(directorio, sonido)
    return sonidos


def cargar_(directory, accept=('.ttf')):
    return cargar_sonidos(directory, accept)


def cargar_todos_sfx(directorio, accept=('.wav')):
    efectos = {}
    for efect in os.listdir(directorio):
        nombre, ext = os.path.splitext(efect)
        if ext.lower() in accept:
            efectos[nombre] = pg.mixer.Sound(os.path.join(directorio, efect))
    return efectos







