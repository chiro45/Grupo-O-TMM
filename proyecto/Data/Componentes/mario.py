

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
        """Establece los tiempos para las animaciones"""
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


    def configuracion_estado_booleanos(self):
        """Configura valores booleanos que afectan el comportamiento de mario"""
        self.frente_derecha = True
        self.permitir_salto = True
        self.muerto = False
        self.invencible = False
        self.grande = False
        self.fuego = False
        self.permitir_bolafuego = True
        self.en_estado_transicion = False
        self.herida_invencible = False
        self.en_castillo = False
        self.agacharse = False
        self.perdiendo_invencibilidad = False


    def configuracion_fuerzas(self):
        """Establece las fuerzas que afectan a la velocidad de Mario"""
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_VEL_CAMINAR
        self.max_y_vel = c.MAX_VEL_Y
        self.x_aceleracion = c.ACELERACION_CAMINAR
        self.vel_salto = c.VEL_SALTO
        self.gravedad = c.GRAVEDAD


    def configuracion_contadores(self):
        """Estos realizan seguimientos totales para varios valores importantes"""
        self.indice_cuadro = 0
        self.indice_invencible = 0
        self.indice_transicion_fuego = 0
        self.conteo_bolas_de_fuego = 0
        self.mastil_bandera_derecha = 0


    def cargar_imagen_desde_hoja(self):
        """Extrae imagenes de mario desde su hoja de configuracion y asigna en las listas apropiadas"""
        self.cuadro_derecho = []
        self.cuadro_izquierdo = []

        self.cuadro_normal_chico_derecho = []
        self.cuadro_normal_chico_izquierdo = []
        self.cuadro_verde_chico_derecho = []
        self.cuadro_verde_chico_izquierdo = []
        self.cuadro_rojo_chico_derecho = []
        self.cuadro_rojo_chico_izquierdo = []
        self.cuadro_negro_chico_derecho = []
        self.cuadro_negro_chico_izquierdo = []

        self.cuadro_normal_grande_derecho = []
        self.cuadro_normal_grande_izquierdo = []
        self.cuadro_verde_grande_derecho = []
        self.cuadro_verde_grande_izquierdo = []
        self.cuadro_rojo_grande_derecho = []
        self.cuadro_rojo_grande_izquierdo = []
        self.cuadro_negro_grande_derecho = []
        self.cuadro_negro_grande_izquierdo = []

        self.cuadro_fuego_derecho = []
        self.cuadro_fuego_izquierdo = []


        #Imagenes para mario normal pequeño#

        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(178, 32, 12, 16))  # Derecha [0]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(80,  32, 15, 16))  # Caminar derecha 1 [1]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(96,  32, 16, 16))  # Caminar derecha 2 [2]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(112,  32, 16, 16))  # Caminar derecha 3 [3]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(144, 32, 16, 16))  # Salto derecha [4]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(130, 32, 14, 16))  # patinaje derecho [5]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(160, 32, 15, 16))  # cuadro de muerte [6]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(320, 8, 16, 24))  # transicion de chico a grande [7]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(241, 33, 16, 16))  # transicion de grande a chico [8]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(194, 32, 12, 16))  # marco 1 del mastil de bandera [9]
        self.cuadro_normal_chico_derecho.append(
            self.get_imagen(210, 33, 12, 16))  # marco 2 del mastil de bandera[10]


        #Imagenes para mario chico verde (animacion invencible)#

        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(178, 224, 12, 16))  # parado derecha [0]
        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(80, 224, 15, 16))  # Caminar derecha 1 [1]
        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(96, 224, 16, 16))  # Caminar derecha 2 [2]
        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(112, 224, 15, 16))  # Caminar derecha 3 [3]
        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(144, 224, 16, 16))  # Salto derecha [4]
        self.cuadro_verde_chico_derecho.append(
            self.get_imagen(130, 224, 14, 16))  # patinaje derecho [5]

        #Imagenes para mario chico rojo (animacion invencible)#

        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(178, 272, 12, 16))  # parado derecha [0]
        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(80, 272, 15, 16))  # Caminar derecha 1 [1]
        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(96, 272, 16, 16))  # Caminar derecha 2 [2]
        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(112, 272, 15, 16))  # Caminar derecha 3 [3]
        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(144, 272, 16, 16))  # Salto derecha [4]
        self.cuadro_rojo_chico_derecho.append(
            self.get_imagen(130, 272, 14, 16))  # patinaje derecho [5]

        #Imagenes para mario negro (animacion invencible)#

        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(178, 176, 12, 16))  # parado derecha [0]
        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(80, 176, 15, 16))  # Caminar derecha 1 [1]
        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(96, 176, 16, 16))  # Caminar derecha 2 [2]
        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(112, 176, 15, 16))  # Caminar derecha 3 [3]
        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(144, 176, 16, 16))  # Salto derecha [4]
        self.cuadro_negro_chico_derecho.append(
            self.get_imagen(130, 176, 14, 16))  # patinaje derecho [5]


        #Imagenes para mario normal grande#

        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(176, 0, 16, 32))  # parado derecha [0]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(81, 0, 16, 32))  # Caminar derecha 1 [1]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(97, 0, 15, 32))  # Caminar derecha 2 [2]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(113, 0, 15, 32))  # Caminar derecha 3 [3]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(144, 0, 16, 32))  # Salto derecha [4]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(128, 0, 16, 32))  # patinaje derecho [5]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(336, 0, 16, 32))  # lanzamiento derecho [6]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(160, 10, 16, 22))  # agacharse derecha [7]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(272, 2, 16, 29))  # Transition grande to small [8]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(193, 2, 16, 30))  # marco 1 del mastil de bandera [9]
        self.cuadro_normal_grande_derecho.append(
            self.get_imagen(209, 2, 16, 29))  # marco 2 del mastil de bandera [10]
       
        #Imagenes para mario verde grande#

        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(176, 192, 16, 32))  # parado derecha [0]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(81, 192, 16, 32))  # Caminar derecha 1 [1]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(97, 192, 15, 32))  # Caminar derecha 2 [2]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(113, 192, 15, 32))  # Caminar derecha 3 [3]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(144, 192, 16, 32))  # Salto derecha [4]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(128, 192, 16, 32))  # patinaje derecho [5]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(336, 192, 16, 32))  # lanzamiento derecho [6]
        self.cuadro_verde_grande_derecho.append(
            self.get_imagen(160, 202, 16, 22))  # agacharse derecha [7]

        #Imagenes para mario rojo grande#

        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(176, 240, 16, 32))  # parado derecha [0]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(81, 240, 16, 32))  # Caminar derecha 1 [1]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(97, 240, 15, 32))  # Caminar derecha 2 [2]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(113, 240, 15, 32))  # Caminar derecha 3 [3]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(144, 240, 16, 32))  # Salto derecha [4]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(128, 240, 16, 32))  # patinaje derecho [5]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(336, 240, 16, 32))  # lanzamiento derecho [6]
        self.cuadro_rojo_grande_derecho.append(
            self.get_imagen(160, 250, 16, 22))  # agacharse derecha [7]

        #Imagenes para mario grande negro#

        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(176, 144, 16, 32))  # parado derecha [0]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(81, 144, 16, 32))  # Caminar derecha 1 [1]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(97, 144, 15, 32))  # Caminar derecha 2 [2]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(113, 144, 15, 32))  # Caminar derecha 3 [3]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(144, 144, 16, 32))  # Salto derecha [4]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(128, 144, 16, 32))  # patinaje derecho [5]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(336, 144, 16, 32))  # lanzamiento derecho [6]
        self.cuadro_negro_grande_derecho.append(
            self.get_imagen(160, 154, 16, 22))  # agacharse derecha [7]


        #Imagenes para mario de fuego#

        self.cuadro_fuego_derecho.append(
            self.get_imagen(176, 48, 16, 32))  # parado derecha [0]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(81, 48, 16, 32))  # Caminar derecha 1 [1]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(97, 48, 15, 32))  # Caminar derecha 2 [2]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(113, 48, 15, 32))  # Caminar derecha 3 [3]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(144, 48, 16, 32))  # Salto derecha [4]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(128, 48, 16, 32))  # patinaje derecho [5]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(336, 48, 16, 32))  # lanzamiento derecho [6]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(160, 58, 16, 22))  # agacharse derecha [7]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(0, 0, 0, 0))  # marcador de posicion [8]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(193, 50, 16, 29))  # marco 1 del mastil de bandera [9]
        self.cuadro_fuego_derecho.append(
            self.get_imagen(209, 50, 16, 29))  # marco 2 del mastil de bandera [10]


        #Los cuadros de la imagen izquierda estan numerados igual que los de la derecha
        #pero los cuadros se invierten

        for cuadro in self.cuadro_normal_chico_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_normal_chico_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_verde_chico_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_verde_chico_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_rojo_chico_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_rojo_chico_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_negro_chico_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_negro_chico_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_normal_grande_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_normal_grande_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_verde_grande_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_verde_grande_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_rojo_grande_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_rojo_grande_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_negro_grande_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_negro_grande_izquierdo.append(nueva_imagen)

        for cuadro in self.cuadro_fuego_derecho:
            nueva_imagen = pg.transform.flip(cuadro, True, False)
            self.cuadro_fuego_izquierdo.append(nueva_imagen)


        self.cuadro_normal_chico = [self.cuadro_normal_chico_derecho,
                              self.cuadro_normal_chico_izquierdo]

        self.cuadro_verde_chico = [self.cuadro_verde_chico_derecho,
                             self.cuadro_verde_chico_izquierdo]

        self.cuadro_rojo_chico = [self.cuadro_rojo_chico_derecho,
                           self.cuadro_rojo_chico_izquierdo]

        self.cuadro_negro_chico = [self.cuadro_negro_chico_derecho,
                             self.cuadro_negro_chico_izquierdo]

        self.listado_cuadro_chico_invencible = [self.cuadro_normal_chico,
                                          self.cuadro_verde_chico,
                                          self.cuadro_rojo_chico,
                                          self.cuadro_negro_chico]

        self.cuadro_normal_grande = [self.cuadro_normal_grande_derecho,
                                  self.cuadro_normal_grande_izquierdo]

        self.cuadro_verde_grande = [self.cuadro_verde_grande_derecho,
                                 self.cuadro_verde_grande_izquierdo]

        self.cuadro_rojo_grande = [self.cuadro_rojo_grande_derecho,
                               self.cuadro_rojo_grande_izquierdo]

        self.cuadro_negro_grande = [self.cuadro_negro_grande_derecho,
                                 self.cuadro_negro_grande_izquierdo]

        self.cuadro_fuego = [self.cuadro_fuego_derecho,
                            self.cuadro_fuego_izquierdo]

        self.listado_cuadro_grande = [self.cuadro_normal_grande,
                                           self.cuadro_verde_grande,
                                           self.cuadro_rojo_grande,
                                           self.cuadro_negro_grande]

        self.todas_imagenes = [self.cuadro_normal_grande_derecho,
                           self.cuadro_negro_grande_derecho,
                           self.cuadro_rojo_grande_derecho,
                           self.cuadro_verde_grande_derecho,
                           self.cuadro_normal_chico_derecho,
                           self.cuadro_verde_chico_derecho,
                           self.cuadro_rojo_chico_derecho,
                           self.cuadro_negro_chico_derecho,
                           self.cuadro_normal_grande_izquierdo,
                           self.cuadro_negro_grande_izquierdo,
                           self.cuadro_rojo_grande_izquierdo,
                           self.cuadro_verde_grande_izquierdo,
                           self.cuadro_normal_chico_izquierdo,
                           self.cuadro_rojo_chico_izquierdo,
                           self.cuadro_verde_chico_izquierdo,
                           self.cuadro_negro_chico_izquierdo]


        self.cuadro_derecho = self.cuadro_normal_chico[0]
        self.cuadro_izquierdo = self.cuadro_normal_chico[1]


    def get_imagen(self, x, y, ancho, alto):
        """Extrae las imagenes de la plantilla"""
        imagen = pg.Surface([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.set_colorkey(c.BLACK)
        imagen = pg.transform.scale(imagen,
                                   (int(rect.ancho*c.MULTIPLICADOR_TAMANIO),
                                    int(rect.alto*c.MULTIPLICADOR_TAMANIO)))
        return imagen


    def actualizar(self, llaves, informacion_juego, grupo_fuego):
        """Actualiza las animaciones de mario un cuadro a la vez"""
        self.tiempo_actual = informacion_juego[c.TIEMPO_ACTUAL]
        self.manejo_estado(llaves, grupo_fuego)
        self.comprueba_estado_especial()
        self.animacion()


    def manejo_estado(self, llaves, grupo_fuego):
        """Determina el comportamiento de mario basado en su estado"""
        if self.estado == c.PARARSE:
            self.parado(llaves, grupo_fuego)
        elif self.estado == c.CAMINAR:
            self.cambinando(llaves, grupo_fuego)
        elif self.estado == c.SALTAR:
            self.saltando(llaves, grupo_fuego)
        elif self.estado == c.CAER:
            self.cayendo(llaves, grupo_fuego)
        elif self.estado == c.SALTO_DE_MUERTE:
            self.saltando_muerte()
        elif self.estado == c.PEQUENIO_A_GRANDE:
            self.cambiando_a_grande()
        elif self.estado == c.GRANDE_A_FUEGO:
            self.cambio_a_fuego()
        elif self.estado == c.GRANDE_A_PEQUENIO:
            self.cambio_a_pequenio()
        elif self.estado == c.MASTILBANDERA:
            self.deslizamiento_bandera()
        elif self.estado == c.BAJO_MASTIL:
            self.sentando_abajo_mastil()
        elif self.estado == c.CAMINANDO_AL_CASTILLO:
            self.caminando_al_castillo()
        elif self.estado == c.CAIDA_FIN_NIVEL:
            self.caida_fin_nivel()


    def parado(self, llaves, grupo_fuego):
        """Esta funcion es llamada si mario sigue de pie"""
        self.verifica_permitir_saltar(llaves)
        self.verifica_permitir_bolafuego(llaves)
        
        self.indice_cuadro = 0
        self.x_vel = 0
        self.y_vel = 0

        if llaves[herramientas.clave_enlace['accion']]:
            if self.fuego and self.permitir_bolafuego:
                self.disparar_bolafuego(grupo_fuego)

        if llaves[herramientas.clave_enlace['abajo']]:
            self.agacharse = True

        if llaves[herramientas.clave_enlace['izquierda']]:
            self.frente_derecha = False
            self.no_agachado()
            self.estado = c.CAMINAR
        elif llaves[herramientas.clave_enlace['right']]:
            self.frente_derecha = True
            self.no_agachado()
            self.estado = c.CAMINAR
        elif llaves[herramientas.clave_enlace['jump']]:
            if self.permitir_salto:
                if self.grande:
                    configuracion.SFX['salgo_grande'].play()
                else:
                    configuracion.SFX['salto_pequenio'].play()
                self.estado = c.SALTAR
                self.y_vel = c.VEL_SALTO
        else:
            self.estado = c.PARARSE

        if not llaves[herramientas.clave_enlace['abajo']]:
            self.no_agachado()


    def no_agachado(self):
        """dejar de estar agachado"""
        abajo = self.rect.abajo
        izquierda = self.rect.x
        if self.frente_derecha:
            self.imagen = self.cuadro_derecho[0]
        else:
            self.imagen = self.cuadro_izquierdo[0]
        self.rect = self.imagen.get_rect()
        self.rect.abajo = abajo
        self.rect.x = izquierda
        self.agacharse = False


    def verifica_permitir_saltar(self, llaves):
        """Verifica si mario puede saltar"""
        if not llaves[herramientas.clave_enlace['salto']]:
            self.permitir_salto = True


    def verifica_permitir_bolafuego(self, llaves):
        """Verifica si puede disparar bolas de fuego"""
        if not llaves[herramientas.clave_enlace['accion']]:
            self.permitir_bolafuego = True

    def disparar_bola_de_fuego(self, superpoder_grupo):
        """Dispara bolas de fuego, permitiendo que no existan más de dos a la vez"""
        configuracion.SFX['bola_de_fuego'].play()
        self.conteo_bolas_de_fuego = self.numero_bolas_fuego(superpoder_grupo)

        if (self.tiempo_actual - self.tiempo_ultima_bolaFuego) > 200:
            if self.conteo_bolas_de_fuego < 2:
                self.permitir_bolafuego = False
                superpoder_grupo.add(
                    potenciadores.BolaFuego(self.rect.derecha, self.rect.y, self.frente_derecha))
                self.tiempo_ultima_bolaFuego = self.tiempo_actual

                self.indice_cuadro = 6
                if self.frente_derecha:
                    self.image = self.cuadro_derecho[self.indice_cuadro]
                else:
                    self.image = self.cuadro_izquierdo[self.indice_cuadro]


    def numero_bolas_fuego(self, superpoder_grupo):
        """Contar el número de bolas de fuego que existen en el nivel"""
        lista_bolasFuego = []

        for superpoder in superpoder_grupo:
            if superpoder.nombre == c.BOLA_DE_FUEGO:
                lista_bolasFuego.append(superpoder)

        return len(lista_bolasFuego)


    def walking(self, llaves, grupo_fuego):
        """Esta función se llama cuando Mario está en un estado de caminar
        Cambia el marco, verifica si se mantiene presionado el botón de ejecución,
        comprueba si hay un salto, luego ajusta el estado si es necesario"""

        self.verificar_permitir_salto(llaves)
        self.verificar_permitir_bolaFuego(llaves)

        if self.indice_cuadro == 0:
            self.indice_cuadro += 1
            self.tiempo_caminando = self.tiempo_actual
        else:
            if (self.tiempo_actual - self.tiempo_caminando >
                    self.calculo_velocidad_animacion()):
                if self.indice_cuadro < 3:
                    self.indice_cuadro += 1
                else:
                    self.indice_cuadro = 1

                self.tiempo_caminando = self.tiempo_actual

        if llaves[herramientas.clave_enlace['accion']]:
            self.max_x_vel = c.MAXIMA_VELOCIDAD_CORRER
            self.x_accel = c.ACELERACION_CORRER
            if self.fuego and self.permitir_bolafuego:
                self.disparar_bola_de_fuego(grupo_fuego)
        else:
            self.max_x_vel = c.MAXIMA_VELOCIDAD_CAMINAR
            self.x_accel = c.ACELERACION_CAMINAR

        if llaves[herramientas.clave_enlace['salto']]:
            if self.permitir_salto:
                if self.grande:
                    configuracion.SFX['salto_grande'].play()
                else:
                    configuracion.SFX['salto_chico'].play()
                self.estado = c.SALTO
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.VELOCIDAD_DE_SALTO - .5
                else:
                    self.y_vel = c.VELOCIDAD_DE_SALTO


        if llaves[herramientas.clave_enlace['izquierda']]:
            self.no_agachado()
            self.frente_derecha = False
            if self.x_vel > 0:
                self.indice_cuadro = 5
                self.x_accel = c.GIRO_PEQUENIO
            else:
                self.x_accel = c.ACELERACION_CAMINAR

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif llaves[herramientas.clave_enlace['right']]:
            self.no_agachado()
            self.frente_derecha = True
            if self.x_vel < 0:
                self.indice_cuadro = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.frente_derecha:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.PARARSE
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.PARARSE


    def calculo_velocidad_animacion(self):
        """Se utiliza para hacer que la velocidad de la animación al caminar esté en relación con
        x-vel de mario"""
        if self.x_vel == 0:
            velocidad_animacion = 130
        elif self.x_vel > 0:
            velocidad_animacion = 130 - (self.x_vel * (13))
        else:
            velocidad_animacion = 130 - (self.x_vel * (13) * -1)

        return velocidad_animacion


    def saltando(self, llaves, grupo_fuego):
        """Llamado cuando Mario está en un estado de SALTO."""
        self.permitir_salto = False
        self.indice_cuadro = 4
        self.gravedad = c.GRAVEDAD_DE_SALTO
        self.y_vel += self.gravedad
        self.verificar_permitir_bolaFuego(llaves)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravedad = c.GRAVEDAD
            self.state = c.CAERSE

        if llaves[herramientas.clave_enlace['izquierda']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif llaves[herramientas.clave_enlace['derecha']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not llaves[herramientas.clave_enlace['salto']]:
            self.gravedad = c.GRAVEDAD
            self.estado = c.CAERSE

        if llaves[herramientas.clave_enlace['accion']]:
            if self.fuego and self.permitir_bolafuego:
                self.disparar_bola_de_fuego(grupo_fuego)


    def cayendo(self, llaves, grupo_fuego):
        """Llamado cuando Mario está en estado de CAÍDA"""
        self.verificar_permitir_bolaFuego(llaves)
        if self.y_vel < c.MAX_VEL_EJEY:
            self.y_vel += self.gravedad

        if llaves[herramientas.clave_enlace['izquierda']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif llaves[herramientas.clave_enlace['derecha']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if llaves[herramientas.clave_enlace['accion']]:
            if self.fuego and self.permitir_bolafuego:
                self.disparar_bola_de_fuego(grupo_fuego)


    def saltando_muerte(self):
        """Llamado cuando Mario está en estado SALTO_MORTAL"""
        if self.temporizador_muerte == 0:
            self.temporizador_muerte = self.tiempo_actual
        elif (self.tiempo_actual - self.temporizador_muerte) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravedad


    def empezar_salto_de_muerte(self, informacion_juego):
        """Usa a Mario en un estado SALTO_MORTAL"""
        self.muerto = True
        informacion_juego[c.MARIO_MUERTO] = True
        self.y_vel = -11
        self.gravedad = .5
        self.indice_cuadro = 6
        self.image = self.cuadro_derecho[self.indice_cuadro]
        self.estado = c.SALTO_MORTAL
        self.en_estado_transicion = True


    def cambio_a_grande(self):
        """Cambia el atributo de imagen de Mario basado en el tiempo mientras
        transición a grande"""
        self.en_estado_transicion = True

        if self.temporizador_transicion == 0:
            self.temporizador_transicion = self.tiempo_actual
        elif self.temporizador_entre_dos_tiempos(135, 200):
            self.poner_mario_imagen_centro()
        elif self.temporizador_entre_dos_tiempos(200, 365):
            self.poner_mario_imagen_pequenia()
        elif self.temporizador_entre_dos_tiempos(365, 430):
            self.poner_mario_imagen_centro()
        elif self.temporizador_entre_dos_tiempos(430, 495):
            self.poner_mario_imagen_pequenia()
        elif self.temporizador_entre_dos_tiempos(495, 560):
            self.poner_mario_imagen_centro()
        elif self.temporizador_entre_dos_tiempos(560, 625):
            self.poner_mario_imagen_grande()
        elif self.temporizador_entre_dos_tiempos(625, 690):
            self.poner_mario_imagen_pequenia()
        elif self.temporizador_entre_dos_tiempos(690, 755):
            self.poner_mario_imagen_centro()
        elif self.temporizador_entre_dos_tiempos(755, 820):
            self.poner_mario_imagen_grande()
        elif self.temporizador_entre_dos_tiempos(820, 885):
            self.poner_mario_imagen_pequenia()
        elif self.temporizador_entre_dos_tiempos(885, 950):
            self.poner_mario_imagen_grande()
            self.state = c.CAMINAR
            self.en_estado_transicion = False
            self.temporizador_transicion = 0
            self.hacerse_grande()


    def temporizador_entre_dos_tiempos(self,inicio, final):
        """Comprueba si el temporizador está en el momento adecuado para la acción."""
        if (self.tiempo_actual - self.temporizador_transicion) >= inicio\
            and (self.tiempo_actual - self.temporizador_transicion) < final:
            return True


    def poner_mario_imagen_centro(self):
        """Durante un cambio de pequeño a grande, establece la imagen de mario en el
        transición/tamaño medio"""
        if self.frente_derecha:
            self.image = self.cuadro_normal_chico[0][7]
        else:
            self.image = self.cuadro_normal_chico[1][7]
        abajo = self.rect.abajo
        centro_x = self.rect.centro_x
        self.rect = self.image.get_rect()
        self.rect.abajo = abajo
        self.rect.centro_x = centro_x


    def poner_mario_imagen_pequenia(self):
        """Durante un cambio de pequeño a grande, establece la imagen de mario en pequeña"""
        if self.frente_derecha:
            self.image = self.cuadro_normal_chico[0][0]
        else:
            self.image = self.cuadro_normal_chico[1][0]
        abajo = self.rect.abajo
        centro_x = self.rect.centro_x
        self.rect = self.image.get_rect()
        self.rect.abajo = abajo
        self.rect.centro_x = centro_x


    def poner_mario_imagen_grande(self):
        """Durante un cambio de pequeño a grande, establece la imagen de mario en grande"""
        if self.frente_derecha:
            self.image = self.cuadro_normal_grande[0][0]
        else:
            self.image = self.cuadro_normal_grande[1][0]
        abajo = self.rect.abajo
        centro_x = self.rect.centro_x
        self.rect = self.image.get_rect()
        self.rect.abajo = abajo
        self.rect.centro_x = centro_x


    def hacerse_grande(self):
        self.grande = True
        self.cuadro_derecho = self.cuadro_normal_grande_derecho
        self.cuadro_izquierdo = self.cuadro_normal_grande_izquierdo
        abajo = self.rect.abajo
        left = self.rect.x
        image = self.cuadro_derecho[0]
        self.rect = image.get_rect()
        self.rect.abajo = abajo
        self.rect.x = left


    def cambio_a_fuego(self):
        """Llamado cuando Mario está en un estado GRANDE_PARA_DISPARAR (es decir, cuando
        obtiene una flor de fuego)"""
        self.en_estado_transicion = True

        if self.frente_derecha:
            cuadros = [self.cuadro_fuego_derecho[3],
                      self.cuadro_verde_grande_derecho[3],
                      self.cuadro_rojo_grande_derecho[3],
                      self.cuadro_negro_grande_derecho[3]]
        else:
            cuadros = [self.cuadro_fuego_izquierdo[3],
                      self.cuadro_verde_grande_izquierdo[3],
                      self.cuadro_rojo_grande_izquierdo[3],
                      self.cuadro_negro_grande_izquierdo[3]]

        if self.temporizador_transicion_fuego == 0:
            self.temporizador_transicion_fuego = self.tiempo_actual
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) > 65 and (self.tiempo_actual - self.temporizador_transicion_fuego) < 130:
            self.image = cuadros[0]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 195:
            self.image = cuadros[1]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 260:
            self.image = cuadros[2]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 325:
            self.image = cuadros[3]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 390:
            self.image = cuadros[0]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 455:
            self.image = cuadros[1]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 520:
            self.image = cuadros[2]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 585:
            self.image = cuadros[3]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 650:
            self.image = cuadros[0]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 715:
            self.image = cuadros[1]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 780:
            self.image = cuadros[2]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 845:
            self.image = cuadros[3]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 910:
            self.image = cuadros[0]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 975:
            self.image = cuadros[1]
        elif (self.tiempo_actual - self.temporizador_transicion_fuego) < 1040:
            self.image = cuadros[2]
            self.fuego = True
            self.en_estado_transicion = False
            self.estado = c.CAMINAR
            self.temporizador_transicion = 0

   
        


    
        