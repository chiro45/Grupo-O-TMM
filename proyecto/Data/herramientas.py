__author__ = 'justinarmstrong'

import os
import pygame as pg

teclasMovimiento = {
    'action':pg.K_e,
    'jump':pg.K_w,
    'left':pg.K_a, 
    'right':pg.K_d,
    'down':pg.K_s
}

class Controles(object):
    
    def __init__(self, titulo):
        self.PANTALLA = pg.display.get_surface()
        self.done = False
        self.tiempo= pg.time.Clock()
        self.titulo = titulo
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()


   

    










