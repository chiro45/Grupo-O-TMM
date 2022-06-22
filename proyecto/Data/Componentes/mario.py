

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


   
        


    
        