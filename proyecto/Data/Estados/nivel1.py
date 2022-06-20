from __futuro__ import division


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
        self.ladrillo_pieces_grupo = pg.sprite.Grupo()

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
        self.mario.actualizar(llaves, self.informacion_juego, self.grupo_encendido)
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
        self.mario.actualizar(llaves, self.informacion_juego, self.grupo_encendido)
        for puntaje in self.lista_puntaje_movil:
            puntaje.actualizar(self.lista_puntaje_movil, self.informacion_juego)
        if self.puntaje_bandera:
            self.puntaje_bandera.actualizar(None, self.informacion_juego)
            self.marca_agregar_puntaje_bandera()
        self.grupo_asta_bandera.actualizar()
        self.puntos_control()
        self.grupo_enemigo.actualizar(self.informacion_juego)
        self.grupo_sprites_mueriendo.actualizar(self.informacion_juego, self.visor)
        self.coraza_grupo.actualizar(self.informacion_juego)
        self.ladrillo_grupo.actualizar()
        self.caja_monedas_grupo.actualizar(self.informacion_juego)
        self.grupo_encendido.actualizar(self.informacion_juego, self.visor)
        self.coin_group.actualizar(self.informacion_juego, self.visor)
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
                if self.mario.rect.bottom < self.bandera.rect.y:
                    self.mario.rect.bottom = self.bandera.rect.y
                self.bandera.estado = c.BAJO_MASTIL
                self.crear_puntos_bandera()

            elif control.nombre == '12':
                self.estado = c.EN_CASTILLO
                self.mario.matar()
                self.mario.estado == c.PARARSE
                self.mario.en_castillo = True
                self.pantalla_informacion_superior.estado = c.CUENTA_REGRESIVA_RAPIDA


            elif control.nombre == 'hongo_secreto' and self.mario.y_vel < 0:
                caja_de_setas = caja_de_monedas.Caja_de_monedas(control.rect.x,
                                        control.rect.bottom - 40,
                                        'hongo',
                                        self.grupo_encendido)
                caja_de_setas.empezar_golpe(self.lista_puntaje_movil)
                self.caja_monedas_grupo.add(caja_de_setas)

                self.mario.y_vel = 7
                self.mario.rect.y = caja_de_setas.rect.bottom
                self.mario.estado = c.CAERSE

            self.mario_y_grupo_enemigo.add(self.grupo_enemigo)


    def crear_puntos_bandera(self):
        """Crea los puntos que aparecen cuando Mario toca el
        asta de bandera"""
        x = 8518
        y = c.ALTURA_DE_SUELO - 60
        mario_bottom = self.mario.rect.bottom

        if mario_bottom > (c.ALTURA_DE_SUELO - 40 - 40):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 100, True)
            self.puntaje_bandera_total = 100
        elif mario_bottom > (c.ALTURA_DE_SUELO - 40 - 160):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 400, True)
            self.puntaje_bandera_total = 400
        elif mario_bottom > (c.ALTURA_DE_SUELO - 40 - 240):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 800, True)
            self.puntaje_bandera_total = 800
        elif mario_bottom > (c.ALTURA_DE_SUELO - 40 - 360):
            self.puntaje_bandera = puntaje.Puntaje(x, y, 2000, True)
            self.puntaje_bandera_total = 2000
        else:
            self.puntaje_bandera = puntaje.Puntaje(x, y, 5000, True)
            self.puntaje_bandera_total = 5000
