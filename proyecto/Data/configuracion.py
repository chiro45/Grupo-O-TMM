

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



GFX   = herramientas.cargar_todos_gfx(os.path.join("Recursos","Graficos"))
SFX   = herramientas.cargar_todos_sfx(os.path.join("Recursos","sonidos"))
MUSICA = herramientas.cargar_sonidos(os.path.join("Recursos","musica"))


