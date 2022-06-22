from __future__ import division


import pygame as pg
from .. import configuracion, herramientas
from .. import constantes as c
from .. import sonido_juego
from .. Componentes import mario
from .. Componentes import colisionador
from .. Componentes import ladrillos
from .. Componentes import caja_monedas
from .. Componentes import enemigos
from .. Componentes import puntoGuardado
from .. Componentes import astaBandera
from .. Componentes import informacion
from .. Componentes import puntaje
from .. Componentes import bandera_castillo


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
        self.configuracion_caja_monedas()
        self.configuracion_bandera_mastil()
        self.configuracion_enemigos()
        self.configuracion_mario()
        self.configuracion_puntoGuardados()
        self.configuracion_spritegrupos()


    def configuracion_fondo(self):
        """Establecer la imagen de fondo, la rectaifica y la dimensiona correctaamente"""
        
        self.fondo = configuracion.GFX['nivel_1']
        self.back_recta = self.fondo.get_recta()
        self.fondo = pg.transform.scale(self.fondo,
                                  (int(self.back_recta.ancho*c.fondo_MULTIPLICADOR),
                                  int(self.back_recta.alto*c.fondo_MULTIPLICADOR)))
        self.back_recta = self.fondo.get_recta()
        ancho = self.back_recta.ancho
        alto = self.back_recta.alto

        self.nivel = pg.Surface((ancho, alto)).convert()
        self.nivel_recta = self.nivel.get_recta()
        self.visor = configuracion.PANTALLA.get_recta(abajo=self.nivel_recta.abajo)
        self.visor.x = self.informacion_juego[c.CAMARA_COMIENZO_X]


    def configuracion_terreno(self):
        """Crea rectaangulos colisionables e invisibles sobre la parte superior del suelo para caminar"""
        terreno_recta1 = colisionador.colisionador(0, c.terreno_alto,    2953, 60)
        terreno_recta2 = colisionador.colisionador(3048, c.terreno_alto,  635, 60)
        terreno_recta3 = colisionador.colisionador(3819, c.terreno_alto, 2735, 60)
        terreno_recta4 = colisionador.colisionador(6647, c.terreno_alto, 2300, 60)

        self.terreno_grupo = pg.sprite.Grupo(terreno_recta1,
                                           terreno_recta2,
                                           terreno_recta3,
                                           terreno_recta4)


    def configuracion_tuberias(self):
        """Crea rectaas colisionables para todas las tuberias"""

        tuberia1 = colisionador.colisionador(1202, 452, 83, 82)
        tuberia2 = colisionador.colisionador(1631, 409, 83, 140)
        tuberia3 = colisionador.colisionador(1973, 366, 83, 170)
        tuberia4 = colisionador.colisionador(2445, 366, 83, 170)
        tuberia5 = colisionador.colisionador(6989, 452, 83, 82)
        tuberia6 = colisionador.colisionador(7675, 452, 83, 82)

        self.grupo_tuberia = pg.sprite.Grupo(tuberia1, tuberia2,
                                          tuberia3, tuberia4,
                                          tuberia5, tuberia6)


    def configuracion_pasos(self):
        """Crea rectaas colisionables para todos los pasos"""
        paso1 = colisionador.colisionador(5745, 495, 40, 44)
        paso2 = colisionador.colisionador(5788, 452, 40, 44)
        paso3 = colisionador.colisionador(5831, 409, 40, 44)
        paso4 = colisionador.colisionador(5874, 366, 40, 176)


        paso5 = colisionador.colisionador(6001, 366, 40, 176)
        paso6 = colisionador.colisionador(6044, 408, 40, 40)
        paso7 = colisionador.colisionador(6087, 452, 40, 40)
        paso8 = colisionador.colisionador(6130, 495, 40, 40)

        paso9 = colisionador.colisionador(6345, 495, 40, 40)
        paso10 = colisionador.colisionador(6388, 452, 40, 40)
        paso11 = colisionador.colisionador(6431, 409, 40, 40)
        paso12 = colisionador.colisionador(6474, 366, 40, 40)
        paso13 = colisionador.colisionador(6517, 366, 40, 176)

        paso14 = colisionador.colisionador(6644, 366, 40, 176)
        paso15 = colisionador.colisionador(6687, 408, 40, 40)
        paso16 = colisionador.colisionador(6728, 452, 40, 40)
        paso17 = colisionador.colisionador(6771, 495, 40, 40)

        paso18 = colisionador.colisionador(7760, 495, 40, 40)
        paso19 = colisionador.colisionador(7803, 452, 40, 40)
        paso20 = colisionador.colisionador(7845, 409, 40, 40)
        paso21 = colisionador.colisionador(7888, 366, 40, 40)
        paso22 = colisionador.colisionador(7931, 323, 40, 40)
        paso23 = colisionador.colisionador(7974, 280, 40, 40)
        paso24 = colisionador.colisionador(8017, 237, 40, 40)
        paso25 = colisionador.colisionador(8060, 194, 40, 40)
        paso26 = colisionador.colisionador(8103, 194, 40, 360)

        paso27 = colisionador.colisionador(8488, 495, 40, 40)

        self.paso_grupo = pg.sprite.Grupo(paso1,  paso2,
                                          paso3,  paso4,
                                          paso5,  paso6,
                                          paso7,  paso8,
                                          paso9,  paso10,
                                          paso11, paso12,
                                          paso13, paso14,
                                          paso15, paso16,
                                          paso17, paso18,
                                          paso19, paso20,
                                          paso21, paso22,
                                          paso23, paso24,
                                          paso25, paso26,
                                          paso27)


    def configuracion_ladrillos(self):
        """Crea todos los ladrillos destruibles para el nivel y grupos para monedas y superpoders o superpoder para
        pasar los ladrillos"""
        self.moneda_grupo = pg.sprite.Grupo()
        self.superpoder_grupo = pg.sprite.Grupo()
        self.grupo_piezas_ladrillos = pg.sprite.Grupo()

        ladrillo1  = ladrillos.ladrillo(858,  365)
        ladrillo2  = ladrillos.ladrillo(944,  365)
        ladrillo3  = ladrillos.ladrillo(1030, 365)
        ladrillo4  = ladrillos.ladrillo(3299, 365)
        ladrillo5  = ladrillos.ladrillo(3385, 365)
        ladrillo6  = ladrillos.ladrillo(3430, 193)
        ladrillo7  = ladrillos.ladrillo(3473, 193)
        ladrillo8  = ladrillos.ladrillo(3516, 193)
        ladrillo9  = ladrillos.ladrillo(3559, 193)
        ladrillo10 = ladrillos.ladrillo(3602, 193)
        ladrillo11 = ladrillos.ladrillo(3645, 193)
        ladrillo12 = ladrillos.ladrillo(3688, 193)
        ladrillo13 = ladrillos.ladrillo(3731, 193)
        ladrillo14 = ladrillos.ladrillo(3901, 193)
        ladrillo15 = ladrillos.ladrillo(3944, 193)
        ladrillo16 = ladrillos.ladrillo(3987, 193)
        ladrillo17 = ladrillos.ladrillo(4030, 365, c.SEISMONEDAS, self.moneda_grupo)
        ladrillo18 = ladrillos.ladrillo(4287, 365)
        ladrillo19 = ladrillos.ladrillo(4330, 365, c.ESTRELLA, self.superpoder_grupo)
        ladrillo20 = ladrillos.ladrillo(5058, 365)
        ladrillo21 = ladrillos.ladrillo(5187, 193)
        ladrillo22 = ladrillos.ladrillo(5230, 193)
        ladrillo23 = ladrillos.ladrillo(5273, 193)
        ladrillo24 = ladrillos.ladrillo(5488, 193)
        ladrillo25 = ladrillos.ladrillo(5574, 193)
        ladrillo26 = ladrillos.ladrillo(5617, 193)
        ladrillo27 = ladrillos.ladrillo(5531, 365)
        ladrillo28 = ladrillos.ladrillo(5574, 365)
        ladrillo29 = ladrillos.ladrillo(7202, 365)
        ladrillo30 = ladrillos.ladrillo(7245, 365)
        ladrillo31 = ladrillos.ladrillo(7331, 365)

        self.ladrillo_grupo = pg.sprite.Grupo(ladrillo1,  ladrillo2,
                                           ladrillo3,  ladrillo4,
                                           ladrillo5,  ladrillo6,
                                           ladrillo7,  ladrillo8,
                                           ladrillo9,  ladrillo10,
                                           ladrillo11, ladrillo12,
                                           ladrillo13, ladrillo14,
                                           ladrillo15, ladrillo16,
                                           ladrillo17, ladrillo18,
                                           ladrillo19, ladrillo20,
                                           ladrillo21, ladrillo22,
                                           ladrillo23, ladrillo24,
                                           ladrillo25, ladrillo26,
                                           ladrillo27, ladrillo28,
                                           ladrillo29, ladrillo30,
                                           ladrillo31)


    def configuracion_caja_monedas(self):
        """Creates all the moneda boxes and puts them in a sprite grupo"""
        caja_monedas1  = caja_monedas.caja_monedas(685, 365, c.MONEDA, self.moneda_grupo)
        caja_monedas2  = caja_monedas.caja_monedas(901, 365, c.HONGO, self.superpoder_grupo)
        caja_monedas3  = caja_monedas.caja_monedas(987, 365, c.MONEDA, self.moneda_grupo)
        caja_monedas4  = caja_monedas.caja_monedas(943, 193, c.MONEDA, self.moneda_grupo)
        caja_monedas5  = caja_monedas.caja_monedas(3342, 365, c.HONGO, self.superpoder_grupo)
        caja_monedas6  = caja_monedas.caja_monedas(4030, 193, c.MONEDA, self.moneda_grupo)
        caja_monedas7  = caja_monedas.caja_monedas(4544, 365, c.MONEDA, self.moneda_grupo)
        caja_monedas8  = caja_monedas.caja_monedas(4672, 365, c.MONEDA, self.moneda_grupo)
        caja_monedas9  = caja_monedas.caja_monedas(4672, 193, c.HONGO, self.superpoder_grupo)
        caja_monedas10 = caja_monedas.caja_monedas(4800, 365, c.MONEDA, self.moneda_grupo)
        caja_monedas11 = caja_monedas.caja_monedas(5531, 193, c.MONEDA, self.moneda_grupo)
        caja_monedas12 = caja_monedas.caja_monedas(7288, 365, c.MONEDA, self.moneda_grupo)

        self.caja_monedas_grupo = pg.sprite.Grupo(caja_monedas1,  caja_monedas2,
                                              caja_monedas3,  caja_monedas4,
                                              caja_monedas5,  caja_monedas6,
                                              caja_monedas7,  caja_monedas8,
                                              caja_monedas9,  caja_monedas10,
                                              caja_monedas11, caja_monedas12)


    def configuracion_bandera_mastil(self):
        """Crea un mastil con bandera al final del nivel"""
        self.bandera = astaBandera.Bandera(8505, 100)

        mastil0 = astaBandera.Mastil(8505, 97)
        mastil1 = astaBandera.Mastil(8505, 137)
        mastil2 = astaBandera.Mastil(8505, 177)
        mastil3 = astaBandera.Mastil(8505, 217)
        mastil4 = astaBandera.Mastil(8505, 257)
        mastil5 = astaBandera.Mastil(8505, 297)
        mastil6 = astaBandera.Mastil(8505, 337)
        mastil7 = astaBandera.Mastil(8505, 377)
        mastil8 = astaBandera.Mastil(8505, 417)
        mastil9 = astaBandera.Mastil(8505, 450)

        finial = astaBandera.Finial(8507, 97)

        self.bandera_mastil_grupo = pg.sprite.Grupo(self.bandera,
                                               finial,
                                               mastil0,
                                               mastil1,
                                               mastil2,
                                               mastil3,
                                               mastil4,
                                               mastil5,
                                               mastil6,
                                               mastil7,
                                               mastil8,
                                               mastil9)


    def configuracion_enemigos(self):
        """Crea a todos los enemigos y los agrupa en una listaa de listaas."""
        goomba0 = enemigos.Goomba()
        goomba1 = enemigos.Goomba()
        goomba2 = enemigos.Goomba()
        goomba3 = enemigos.Goomba()
        goomba4 = enemigos.Goomba(193)
        goomba5 = enemigos.Goomba(193)
        goomba6 = enemigos.Goomba()
        goomba7 = enemigos.Goomba()
        goomba8 = enemigos.Goomba()
        goomba9 = enemigos.Goomba()
        goomba10 = enemigos.Goomba()
        goomba11 = enemigos.Goomba()
        goomba12 = enemigos.Goomba()
        goomba13 = enemigos.Goomba()
        goomba14 = enemigos.Goomba()
        goomba15 = enemigos.Goomba()

        koopa0 = enemigos.Koopa()

        enemigo_grupo1 = pg.sprite.Grupo(goomba0)
        enemigo_grupo2 = pg.sprite.Grupo(goomba1)
        enemigo_grupo3 = pg.sprite.Grupo(goomba2, goomba3)
        enemigo_grupo4 = pg.sprite.Grupo(goomba4, goomba5)
        enemigo_grupo5 = pg.sprite.Grupo(goomba6, goomba7)
        enemigo_grupo6 = pg.sprite.Grupo(koopa0)
        enemigo_grupo7 = pg.sprite.Grupo(goomba8, goomba9)
        enemigo_grupo8 = pg.sprite.Grupo(goomba10, goomba11)
        enemigo_grupo9 = pg.sprite.Grupo(goomba12, goomba13)
        enemigo_grupo10 = pg.sprite.Grupo(goomba14, goomba15)

        self.enemigo_grupo_lista = [enemigo_grupo1,
                                 enemigo_grupo2,
                                 enemigo_grupo3,
                                 enemigo_grupo4,
                                 enemigo_grupo5,
                                 enemigo_grupo6,
                                 enemigo_grupo7,
                                 enemigo_grupo8,
                                 enemigo_grupo9,
                                 enemigo_grupo10]


    def configuracion_mario(self):
        """Pone a Mario en el principio del nivel"""
        self.mario = mario.Mario()
        self.mario.recta.x = self.visor.x + 110
        self.mario.recta.abajo = c.terreno_alto


    def configuracion_puntoGuardados(self):
        """Crea puntos invisibles de guardado que al tocarlos activa la creacion de enemigos
        guardados en  self.enemigos_grupo_lista"""
        pcontrol1 = puntoGuardado.puntoGuardado(510, "1")
        pcontrol2 = puntoGuardado.puntoGuardado(1400, '2')
        pcontrol3 = puntoGuardado.puntoGuardado(1740, '3')
        pcontrol4 = puntoGuardado.puntoGuardado(3080, '4')
        pcontrol5 = puntoGuardado.puntoGuardado(3750, '5')
        pcontrol6 = puntoGuardado.puntoGuardado(4150, '6')
        pcontrol7 = puntoGuardado.puntoGuardado(4470, '7')
        pcontrol8 = puntoGuardado.puntoGuardado(4950, '8')
        pcontrol9 = puntoGuardado.puntoGuardado(5100, '9')
        pcontrol10 = puntoGuardado.puntoGuardado(6800, '10')
        pcontrol11 = puntoGuardado.puntoGuardado(8504, '11', 5, 6)
        pcontrol12 = puntoGuardado.puntoGuardado(8775, '12')
        pcontrol13 = puntoGuardado.puntoGuardado(2740, 'secret_HONGO', 360, 40, 12)

        self.pcontrol_punto_grupo = pg.sprite.Grupo(pcontrol1, pcontrol2, pcontrol3,
                                                 pcontrol4, pcontrol5, pcontrol6,
                                                 pcontrol7, pcontrol8, pcontrol9,
                                                 pcontrol10, pcontrol11, pcontrol12,
                                                 pcontrol13)


    def configuracion_spritegrupos(self):
        """Sprite grupos creados por conveniencia"""
        self.sprites_sobre_muerte_en_grupo = pg.sprite.Grupo()
        self.coraza_grupo = pg.sprite.Grupo()
        self.grupo_enemigo = pg.sprite.Grupo()

        self.terreno_paso_grupo_tuberia = pg.sprite.Grupo(self.terreno_grupo,
                                                      self.grupo_tuberia,
                                                      self.paso_grupo)

        self.mario_y_grupo_enemigo = pg.sprite.Grupo(self.mario,
                                                     self.grupo_enemigo)


    def actualizar(self, superficie, llaves, tiempo_actual):
        """Updates Entire nivel using estados.  Called by the control object"""
        self.informacion_juego[c.tiempo_actual] = self.tiempo_actual = tiempo_actual
        self.manejo_Estados(llaves)
        self.pcontrol_si_sin_tiempo()
        self.arruinar_todo(superficie)
        self.administracion_sonido.actualizar(self.informacion_juego, self.mario)

    def manejo_estados(self, llaves):
        """Si el nivel está en estado CONGELADO, solo Mario se actualizará."""
        if self.estado == c.FRIZADO:
            self.actualizar_estado_transicion(llaves)
        elif self.estado == c.NO_FRIZADO:
            self.atualizar_sprites(llaves)
        elif self.estado == c.EN_CASTILLO:
            self.actualizar_castillo()
        elif self.estado == c.BANDERA_FUEGOSARTIFICIALES:
            self.actualizar_bandera_fuegosArtificiales()


    def actualizar_en_estado_transicion(self, llaves):
        """Actualiza a mario en un estado de transición. Comprueba si deja el estado de transición o muere para volver a cambiar el estado del nivel"""
        self.mario.actualizar(llaves, self.informacion_juego, self.superpoder_grupo)
        for puntaje in self.lista_puntaje_movil:
            puntaje.actualizar(self.lista_puntaje_movil, self.informacion_juego)
        if self.puntaje_bandera:
            self.puntaje_bandera.actualizar(None, self.informacion_juego)
            self.marca_agregar_puntaje_bandera()
        self.caja_monedas_grupo.actualizar(self.informacion_juego)
        self.grupo_asta_bandera.actualizar(self.informacion_juego)
        self.comprobacion_mario_estado_transicion()
        self.marcar_bandera()
        self.comprobacion_muerte_mario()
        self.pantalla_informacion_superior.actualizar(self.informacion_juego, self.mario)

    def comprobacion_mario_estado_transicion(self):
        """Si mario está en un estado de transición, el nivel estará en CONGELACIÓN estado"""
        if self.mario.en_estado_transicion:
            self.informacion_juego[c.ESTADO_DEL_NIVEL] = self.estado = c.FRIZADO
        elif self.mario.en_estado_transicion == False:
            if self.estado == c.FRIZADO:
                self.informacion_juego[c.ESTADO_DEL_NIVEL] = self.estado = c.NO_FRIZADO


    def actualizar_sprites(self, llaves):
        """Actualiza la ubicación de todos los sprites en la pantalla."""
        self.mario.actualizar(llaves, self.informacion_juego, self.superpoder_grupo)
        for puntaje in self.lista_puntaje_movil:
            puntaje.actualizar(self.lista_puntaje_movil, self.informacion_juego)
        if self.puntaje_bandera:
            self.puntaje_bandera.actualizar(None, self.informacion_juego)
            self.marca_agregar_puntaje_bandera()
        self.grupo_asta_bandera.actualizar()
        self.puntos_control()
        self.grupo_enemigo.actualizar(self.informacion_juego)
        self.sprites_sobre_muerte_en_grupo.actualizar(self.informacion_juego, self.visor)
        self.coraza_grupo.actualizar(self.informacion_juego)
        self.ladrillo_grupo.actualizar()
        self.caja_monedas_grupo.actualizar(self.informacion_juego)
        self.superpoder_grupo.actualizar(self.informacion_juego, self.visor)
        self.moneda_grupo.actualizar(self.informacion_juego, self.visor)
        self.grupo_piezas_ladrillos.actualizar()
        self.ajustar_posicion_sprite()
        self.comprobacion_mario_estado_transicion()
        self.comprobacion_muerte_mario()
        self.actualizar_visor()
        self.pantalla_informacion_superior.actualizar(self.informacion_juego, self.mario)

    def puntos_control(self):
        """Detectar si se produce una colisión de puntos de control, eliminar puntos de control,
        agregar enemigos a self.enemy_group"""
        control = pg.sprite.spritecollideany(self.mario,
                                                 self.pcontrol_punto_grupo)
        if control:
            control.kill()

            for i in range(1,11):
                if control.nombre == str(i):
                    for indice, enemigo in enumerate(self.enemigo_grupo_lista[i -1]):
                        enemigo.rect.x = self.visor.derecha + (indice * 60)
                    self.grupo_enemigo.add(self.enemigo_grupo_lista[i-1])

            if control.nombre == '11':
                self.mario.estado = c.ASTA_DE_BANDERA
                self.mario.invincible = False
                self.mario.asta_bandera_derecha = control.rect.derecha
                if self.mario.rect.abajo < self.bandera.rect.y:
                    self.mario.rect.abajo = self.bandera.rect.y
                self.bandera.estado = c.BAJO_MASTIL
                self.crear_puntos_bandera()

            elif control.nombre == '12':
                self.estado = c.EN_CASTILLO
                self.mario.kill()
                self.mario.estado == c.PARARSE
                self.mario.en_castillo = True
                self.pantalla_informacion_superior.estado = c.CUENTA_REGRESIVA_RAPIDA


            elif control.nombre == 'hongo_secreto' and self.mario.y_vel < 0:
                caja_de_setas = caja_de_monedas.Caja_de_monedas(control.rect.x,
                                        control.rect.abajo - 40,
                                        'hongo',
                                        self.superpoder_grupo)
                caja_de_setas.empezar_golpe(self.lista_puntaje_movil)
                self.caja_monedas_grupo.add(caja_de_setas)

                self.mario.y_vel = 7
                self.mario.rect.y = caja_de_setas.rect.abajo
                self.mario.estado = c.CAERSE

            self.mario_y_grupo_enemigo.add(self.grupo_enemigo)


    def crear_puntos_bandera(self):
        """Crea los puntos que aparecen cuando Mario toca el
        asta de bandera"""
        x = 8518
        y = c.ALTURA_DE_SUELO - 60
        mario_abajo = self.mario.rect.abajo

        if mario_abajo > (c.ALTURA_DE_SUELO - 40 - 40):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 100, True)
            self.puntaje_bandera_total = 100
        elif mario_abajo > (c.ALTURA_DE_SUELO - 40 - 160):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 400, True)
            self.puntaje_bandera_total = 400
        elif mario_abajo > (c.ALTURA_DE_SUELO - 40 - 240):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 800, True)
            self.puntaje_bandera_total = 800
        elif mario_abajo > (c.ALTURA_DE_SUELO - 40 - 360):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 2000, True)
            self.puntaje_bandera_total = 2000
        else:
            self.puntaje_bandera = puntaje.Puntaje(x, y, 5000, True)
            self.puntaje_bandera_total = 5000

    def ajustar_posicion_sprite(self):
        """Ajusta los sprites por sus velocidades x e y y colisiones"""
        self.ajustar_posicion_mario()
        self.ajustar_posicion_enemigo()
        self.ajustar_posicion_caparazon()
        self.ajustar_posicion_encendido()


    def ajustar_posicion_mario(self):
        """Ajusta la posición de Mario en función de sus velocidades x, y y
        posibles colisiones"""
        self.ultima_posicion_x = self.mario.rect.derecha
        self.mario.rect.x += round(self.mario.x_vel)
        self.comprobar_mario_x_colisiones()

        if self.mario.en_estado_transicion == False:
            self.mario.rect.y += round(self.mario.y_vel)
            self.comprobar_mario_y_colisiones()

        if self.mario.rect.x < (self.ventana_grafica.x + 5):
            self.mario.rect.x = (self.ventana_grafica.x + 5)


    def comprobar_mario_x_colisiones(self):
        """Compruebe si hay colisiones después de mover a Mario en el eje x"""
        colisionador = pg.sprite.spritecollideany(self.mario, self.terreno_paso_grupo_tuberia)
        caja_monedas = pg.sprite.spritecollideany(self.mario, self.caja_monedas_grupo)
        ladrillo = pg.sprite.spritecollideany(self.mario, self.ladrillo_grupo)
        enemigo = pg.sprite.spritecollideany(self.mario, self.grupo_enemigo)
        coraza = pg.sprite.spritecollideany(self.mario, self.coraza_grupo)
        superpoder = pg.sprite.spritecollideany(self.mario, self.superpoder_grupo)

        if caja_monedas:
            self.ajustar_mario_para_x_colisiones(caja_monedas)

        elif ladrillo:
            self.ajustar_mario_para_x_colisiones(ladrillo)

        elif colisionador:
            self.ajustar_mario_para_x_colisiones(colisionador)

        elif enemigo:
            if self.mario.invincible:
                configuracion.SFX['kick'].play()
                self.informacion_juego[c.PUNTAJE] += 100
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(self.mario.rect.derecha - self.visor.x,
                                self.mario.rect.y, 100))
                enemigo.kill()
                enemigo.empezar_salto_de_muerte(c.DERECHA)
                self.sprites_sobre_muerte_en_grupo.add(enemigo)
            elif self.mario.grande:
                configuracion.SFX['tubo'].play()
                self.mario.fuego = False
                self.mario.y_vel = -1
                self.mario.estado = c.GRANDE_A_PEQUENIO
                self.convertir_floresFuego_en_hongos()
            elif self.mario.herida_invencible:
                pass
            else:
                self.mario.empezar_salto_de_muerte(self.informacion_juego)
                self.estado = c.FRIZADO

        elif coraza:
            self.ajustar_mario_para_x_colisiones_coraza(coraza)

        elif superpoder:
            if superpoder.nombre == c.ESTRELLA:
                self.informacion_juego[c.PUNTAJE] += 1000

                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(self.mario.rect.centro_x - self.visor.x,
                                self.mario.rect.y, 1000))
                self.mario.invincible = True
                self.mario.temporizador_inicio_invencible = self.tiempo_actual
            elif superpoder.name == c.HONGOS:
                configuracion.SFX['superpoder'].play()
                self.informacion_juego[c.PUNTAJE] += 1000
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(self.mario.rect.centro_x - self.visor.x,
                                self.mario.rect.y - 20, 1000))

                self.mario.y_vel = -1
                self.mario.estadp = c.PEQUENIO_A_GRANDE
                self.mario.en_estado_transicion = True
                self.convertir_hongos_en_floresFuego()
            elif superpoder.nombre == c.HONGO_DE_VIDA:
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(superpoder.rect.derecha - self.visor.x,
                                superpoder.rect.y,
                                c.UNA_VIDA))

                self.informacion_juego[c.VIDAS] += 1
                configuracion.SFX['una_vida'].play()
            elif superpoder.nombre == c.FLOR_FUEGO:
                configuracion.SFX['superpoder'].play()
                self.informacion_juego[c.PUNTAJE] += 1000
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(self.mario.rect.centro_x - self.visor.x,
                                self.mario.rect.y, 1000))

                if self.mario.grande and self.mario.fuego == False:
                    self.mario.estado = c.GRANDE_PARA_DISPARAR
                    self.mario.en_estado_transicion = True
                elif self.mario.grande == False:
                    self.mario.estado = c.PEQUENIO_A_GRANDE
                    self.mario.en_estado_transicion = True
                    self.convertir_hongos_en_floresFuego()

            if superpoder.nombre != c.BOLA_DE_FUEGO:
                superpoder.kill()


    def convertir_hongos_en_floresFuego(self):
        """Cuando Mario se vuelve grande, convierte todos los potenciadores de flores de fuego en
        potenciadores de hongos"""
        for ladrillo in self.ladrillo_grupo:
            if ladrillo.contenido == c.HONGO:
                ladrillo.contenido = c.FLOR_FUEGO
        for caja_monedas in self.moneda_grupo:
            if caja_monedas.contenido == c.HONGO:
                caja_monedas.contenido = c.FLOR_FUEGO


    def convertir_floresFuego_en_hongos(self):
        """Cuando Mario se hace pequeño, convierte todos los potenciadores de setas en
        potenciadores de flores de fuego"""
        for ladrillo in self.ladrillo_grupo:
            if ladrillo.contenido == c.FLOR_FUEGO:
                ladrillo.contenido = c.HONGO
        for caja_monedas in self.moneda_grupo:
            if caja_monedas.contenido == c.FLOR_FUEGO:
                caja_monedas.contenido = c.HONGO


    def ajustar_mario_para_x_colisiones(self, colisionador):
        """Pone a Mario al ras junto al colisionador después de moverse en el eje x"""
        if self.mario.rect.x < colisionador.rect.x:
            self.mario.rect.derecha = colisionador.rect.izquierda
        else:
            self.mario.rect.izquierda = colisionador.rect.derecha

        self.mario.x_vel = 0

    def ajustar_mario_para_x_colisiones_coraza(self, coraza):
        """Trata con Mario si golpea un proyectil que se mueve en el eje x"""
        if coraza.estado == c.SALTO_SOBRE:
            if self.mario.rect.x < coraza.rect.x:
                self.informacion_juego[c.PUNTAJE] += 400
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(coraza.rect.centro_x - self.visor.x,
                                coraza.rect.y,
                                400))
                self.mario.rect.derecha = coraza.rect.izquierda
                coraza.direccion = c.DERECHA
                coraza.x_vel = 5
                coraza.rect.x += 5

            else:
                self.mario.rect.izquierda = coraza.rect.derecha
                coraza.direccion = c.IZQUIERDA
                coraza.x_vel = -5
                coraza.rect.x += -5

            coraza.estado = c.DESLICE_DE_CAPARAZON

        elif coraza.estado == c.DESLICE_DE_CAPARAZON:
            if self.mario.grande and not self.mario.invincible:
                self.mario.estado = c.GRANDE_A_PEQUENIO
            elif self.mario.invincible:
                self.informacion_juego[c.PUNTAJE] += 200
                self.lista_puntaje_movil.append(
                    puntaje.Puntaje(coraza.rect.derecha - self.visor.x,
                                coraza.rect.y, 200))
                coraza.kill()
                self.sprites_sobre_muerte_en_grupo.add(coraza)
                coraza.empezar_salto_de_muerte(c.DERECHA)
            else:
                if not self.mario.herida_invencible and not self.mario.invincible:
                    self.estado = c.FRIZADO
                    self.mario.empezar_salto_de_muerte(self.informacion_juego)


    def comprobar_mario_y_colisiones(self):
        """Comprueba si hay colisiones cuando Mario se mueve a lo largo del eje y"""
        paso_tierra_o_tuberia = pg.sprite.spritecollideany(self.mario, self.terreno_paso_grupo_tuberia)
        enemigo = pg.sprite.spritecollideany(self.mario, self.grupo_enemigo)
        coraza = pg.sprite.spritecollideany(self.mario, self.coraza_grupo)
        ladrillo = pg.sprite.spritecollideany(self.mario, self.ladrillo_grupo)
        caja_monedas = pg.sprite.spritecollideany(self.mario, self.caja_monedas_grupo)
        superpoder = pg.sprite.spritecollideany(self.mario, self.superpoder_grupo)

        ladrillo, caja_monedas = self.prevenir_conflicto_de_colision(ladrillo, caja_monedas)

        if caja_monedas:
            self.ajustar_mario_para_colisiones_caja_monedas_y(caja_monedas)

        elif ladrillo:
            self.ajustar_mario_para_colisiones_ladrillos_y(ladrillo)

        elif paso_tierra_o_tuberia:
            self.ajustar_mario_para_colisiones_tuberiaTierra_y(paso_tierra_o_tuberia)

        elif enemigo:
            if self.mario.invincible:
                configuracion.SFX['patada'].play()
                enemigo.kill()
                self.sprites_sobre_muerte_en_grupo.add(enemigo)
                enemigo.empezar_salto_de_muerte(c.DERECHA)
            else:
                self.ajustar_mario_para_colisiones_enemigas_y(enemigo)

        elif coraza:
            self.ajustar_mario_para_colisiones_coraza_y(coraza)

        elif superpoder:
            if superpoder.nombre == c.ESTRELLA:
                configuracion.SFX['superpoder'].play()
                superpoder.kill()
                self.mario.invincible = True
                self.mario.invincible_start_timer = self.tiempo_actual

        self.prueba_si_mario_cae()


    def prevenir_conflicto_de_colision(self, obstaculo1, obstaculo2):
        """Permite colisiones solo para el elemento más cercano a marios centerx"""
        if obstaculo1 and obstaculo2:
            distancia_obstaculo1 = self.mario.rect.centro_x - obstaculo1.rect.centro_x
            if distancia_obstaculo1 < 0:
                distancia_obstaculo1 *= -1
            distancia_obstaculo2 = self.mario.rect.centro_x - obstaculo2.rect.centro_x
            if distancia_obstaculo2 < 0:
                distancia_obstaculo2 *= -1

            if distancia_obstaculo1 < distancia_obstaculo2:
                obstaculo2 = False
            else:
                obstaculo1 = False

        return obstaculo1, obstaculo2


    def ajustar_mario_para_colisiones_caja_monedas_y(self, caja_monedas):
        """Mario colisiona con cajas de monedas en el eje y"""
        if self.mario.rect.y > caja_monedas.rect.y:
            if caja_monedas.estado == c.LADRILLO_EN_REPOSO:
                if caja_monedas.contenido == c.MONEDA:
                    self.informacion_juego[c.PUNTAJE] += 200
                    caja_monedas.empezar_golpe(self.lista_puntaje_movil)
                    if caja_monedas.contenido == c.MONEDA:
                        self.informacion_juego[c.TOTAL_MONEDAS] += 1
                else:
                    caja_monedas.empezar_golpe(self.lista_puntaje_movil)

            elif caja_monedas.estado == c.ABIERTA:
                pass
            configuracion.SFX['golpe'].play()
            self.mario.y_vel = 7
            self.mario.rect.y = caja_monedas.rect.bottom
            self.mario.estado = c.CAERSE
        else:
            self.mario.y_vel = 0
            self.mario.rect.abajo = caja_monedas.rect.arriba
            self.mario.estado = c.CAMINAR

    def ajustar_mario_para_colisiones_ladrillos_y(self, ladrillo):
        """Mario colisiona con ladrillos en el eje y"""
        if self.mario.rect.y > ladrillo.rect.y:
            if ladrillo.estado == c.LADRILLO_EN_REPOSO:
                if self.mario.grande and ladrillo.contenido is None:
                    configuracion.SFX['aplastar_ladrillos'].play()
                    self.comprueba_enemigo_en_ladrillo(ladrillo)
                    ladrillo.kill()
                    self.grupo_piezas_ladrillo.add(
                        ladrillos.PiezasLadrillo(ladrillo.rect.x,
                                               ladrillo.rect.y - (ladrillo.rect.altura/2),
                                               -2, -12),
                        ladrillos.PiezasLadrillo(ladrillo.rect.derecha,
                                               ladrillo.rect.y - (ladrillo.rect.altura/2),
                                               2, -12),
                        ladrillos.PiezasLadrillo(ladrillo.rect.x,
                                               ladrillo.rect.y,
                                               -2, -6),
                        ladrillos.PiezasLadrillo(ladrillo.rect.derecha,
                                               ladrillo.rect.y,
                                               2, -6))
                else:
                    configuracion.SFX['golpe'].play()
                    if ladrillo.total_monedas > 0:
                        self.informacion_juego[c.TOTAL_MONEDAS] += 1
                        self.informacion_juego[c.PUNTAJE] += 200
                    self.comprueba_enemigo_en_ladrillo(ladrillo)
                    ladrillo.empezar_golpe(self.lista_puntaje_movil)
            elif ladrillo.estado == c.ABIERTA:
                configuracion.SFX['golpe'].play()
            self.mario.y_vel = 7
            self.mario.rect.y = ladrillo.rect.abajo
            self.mario.estado = c.CAERSE

        else:
            self.mario.y_vel = 0
            self.mario.rect.abajo = ladrillo.rect.arriba
            self.mario.estado = c.CAMINAR


    def comprueba_enemigo_en_ladrillo(self, ladrillo):
        """Mata al enemigo si está en un ladrillo golpeado o roto"""
        ladrillo.rect.y -= 5

        enemigo = pg.sprite.spritecollideany(ladrillo, self.grupo_enemigo)

        if enemigo:
            configuracion.SFX['patada'].play()
            self.informacion_juego[c.PUNTAJE] += 100
            self.lista_puntaje_movil.append(
                puntaje.Puntaje(enemigo.rect.centro_x - self.visor.x,
                            enemigo.rect.y,
                            100))
            enemigo.kill()
            self.sprites_sobre_muerte_en_grupo.add(enemigo)
            if self.mario.rect.centro_x > ladrillo.rect.centro_x:
                enemigo.empezar_salto_de_muerte('derecha')
            else:
                enemigo.empezar_salto_de_muerte('izquierda')

        ladrillo.rect.y += 5



    def ajustar_mario_para_colisiones_tuberiaTierra_y(self, colisionador):
        """Mario choca con tuberías en el eje y"""
        if colisionador.rect.abajo > self.mario.rect.abajo:
            self.mario.y_vel = 0
            self.mario.rect.abajo = colisionador.rect.arriba
            if self.mario.estado == c.FIN_DEL_NIVEL:
                self.mario.estado = c.CAMINANDO_AL_CASTILLO
            else:
                self.mario.estado = c.CAMINAR
        elif colisionador.rect.arriba < self.mario.rect.arriba:
            self.mario.y_vel = 7
            self.mario.rect.arriba = colisionador.rect.abajo
            self.mario.estado = c.CAERSE


    def prueba_si_mario_cae(self):
        """Cambia a Mario a un estado de CAÍDA si hay más de un píxel por encima de una tubería,
        suelo, escalón o caja"""
        self.mario.rect.y += 1
        grupo_prueba_de_colision = pg.sprite.Group(self.terreno_paso_grupo_tuberia,
                                                 self.ladrillo_grupo,
                                                 self.caja_monedas_grupo)


        if pg.sprite.spritecollideany(self.mario, grupo_prueba_de_colision) is None:
            if self.mario.estado != c.SALTO \
                and self.mario.estado != c.SALTO_MORTAL \
                and self.mario.estado != c.PEQUENIO_A_GRANDE \
                and self.mario.estado != c.GRANDE_PARA_DISPARAR \
                and self.mario.estado != c.GRANDE_A_PEQUENIO \
                and self.mario.estado != c.ASTA_DE_BANDERA \
                and self.mario.estado != c.CAMINANDO_AL_CASTILLO \
                and self.mario.estado != c.FIN_DEL_NIVEL:
                self.mario.estado = c.FALL
            elif self.mario.estado == c.CAMINANDO_AL_CASTILLO or \
                self.mario.estado == c.FIN_DEL_NIVEL:
                self.mario.estado = c.FIN_DEL_NIVEL

        self.mario.rect.y -= 1
