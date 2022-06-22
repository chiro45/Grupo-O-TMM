

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

   
        


    
        