

import os
import pygame as pg
from . import herramientas
from .import constantes as c

#en este archivo tenemos la configuracion

TITULO_ORIGINAL = c.TITULO_ORIGINAL



os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.TITULO_ORIGINAL)
PANTALLA = pg.display.set_mode(c.TAMAÑO_PANTALLA)
PANTALLA_RECTANGULAR = PANTALLA.get_rect()



MUSICA = herramientas.load_all_music(os.path.join("Recursos","musica"))
GFX   = herramientas.load_all_gfx(os.path.join("Recursos","Graficos"))
SFX   = herramientas.load_all_sfx(os.path.join("Recursos","sonidos"))


