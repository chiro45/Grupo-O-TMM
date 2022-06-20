
from re import X
import pygame as pg
from .. import configuracion
from .. import constantes as c
from . import efecto_moneda


class Personaje(pg.sprite.Sprite):
    """Clase principal para todos los personajes utilizados en informacion general del nivel"""
    def __init__(self, imagen):
        super(Personaje, self).__init__()
        self.imagen = imagen
        self.rect = self.imagen.get_rect()


class InformacionGeneral(object):
    """Clase para ver la informacion del nivel, puntaje, monedas, tiempo restante"""
    def __init__(self, informacion_juego, estado):
        self.sprite_sheet = configuracion.GFX['imagenes_texto']
        self.total_monedas = informacion_juego[c.TOTAL_MONEDAS]
        self.tiempo = 401
        self.tiempo_actual = 0
        self.total_vidas = informacion_juego[c.VIDAS]
        self.mejor_puntaje = informacion_juego[c.MEJOR_PUNTAJE]
        self.estado = estado
        self.estado_especial = None
        self.informacion_juego = informacion_juego

        self.create_imagen_dict()
        self.create_grupo_puntaje()
        self.create_etiqueta_informacion()
        self.create_etiqueta_pantalla_carga()
        self.create_reloj_cuentatras()
        self.create_contador_monedas()
        self.create_efecto_moneda()
        self.create_mario_imagen()
        self.create_etiqueta_juego_terminado()
        self.create_etiqueta_tiempo_terminado()
        self.create_etiqueta_menu_principal()


    def create_imagen_dict(self):
        """Crea la imagen inicial para el puntaje"""
        self.imagen_dict = {}
        imagen_list = []

        imagen_list.append(self.get_imagen(3, 230, 7, 7))
        imagen_list.append(self.get_imagen(12, 230, 7, 7))
        imagen_list.append(self.get_imagen(19, 230, 7, 7))
        imagen_list.append(self.get_imagen(27, 230, 7, 7))
        imagen_list.append(self.get_imagen(35, 230, 7, 7))
        imagen_list.append(self.get_imagen(43, 230, 7, 7))
        imagen_list.append(self.get_imagen(51, 230, 7, 7))
        imagen_list.append(self.get_imagen(59, 230, 7, 7))
        imagen_list.append(self.get_imagen(67, 230, 7, 7))
        imagen_list.append(self.get_imagen(75, 230, 7, 7))

        imagen_list.append(self.get_imagen(83, 230, 7, 7))
        imagen_list.append(self.get_imagen(91, 230, 7, 7))
        imagen_list.append(self.get_imagen(99, 230, 7, 7))
        imagen_list.append(self.get_imagen(107, 230, 7, 7))
        imagen_list.append(self.get_imagen(115, 230, 7, 7))
        imagen_list.append(self.get_imagen(123, 230, 7, 7))
        imagen_list.append(self.get_imagen(3, 238, 7, 7))
        imagen_list.append(self.get_imagen(11, 238, 7, 7))
        imagen_list.append(self.get_imagen(20, 238, 7, 7))
        imagen_list.append(self.get_imagen(27, 238, 7, 7))
        imagen_list.append(self.get_imagen(35, 238, 7, 7))
        imagen_list.append(self.get_imagen(44, 238, 7, 7))
        imagen_list.append(self.get_imagen(51, 238, 7, 7))
        imagen_list.append(self.get_imagen(59, 238, 7, 7))
        imagen_list.append(self.get_imagen(67, 238, 7, 7))
        imagen_list.append(self.get_imagen(75, 238, 7, 7))
        imagen_list.append(self.get_imagen(83, 238, 7, 7))
        imagen_list.append(self.get_imagen(91, 238, 7, 7))
        imagen_list.append(self.get_imagen(99, 238, 7, 7))
        imagen_list.append(self.get_imagen(108, 238, 7, 7))
        imagen_list.append(self.get_imagen(115, 238, 7, 7))
        imagen_list.append(self.get_imagen(123, 238, 7, 7))
        imagen_list.append(self.get_imagen(3, 246, 7, 7))
        imagen_list.append(self.get_imagen(11, 246, 7, 7))
        imagen_list.append(self.get_imagen(20, 246, 7, 7))
        imagen_list.append(self.get_imagen(27, 246, 7, 7))
        imagen_list.append(self.get_imagen(48, 248, 7, 7))

        imagen_list.append(self.get_imagen(68, 249, 6, 2))
        imagen_list.append(self.get_imagen(75, 247, 6, 6))



        cadena_caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for caracter, imagen in zip(cadena_caracteres, imagen_list):
            self.imagen_dict[caracter] = imagen


    def get_imagen(self, x, y, ancho, alto):
        """Extrae imagen de sprite sheet"""
        imagen = pg.Surface([ancho, alto])
        rect = imagen.get_rect()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto))
        imagen.set_colorkey((92, 148, 252))
        imagen = pg.transform.scale(imagen,
                                   (int(rect.ancho*2.9),
                                    int(rect.alto*2.9)))
        return imagen


    def create_grupo_puntaje(self):
        """Crea el puntaje inicial vacio (000000)"""
        self.imagen_puntaje = []
        self.create_etiqueta(self.imagen_puntaje, '000000', 75, 55)


    def create_etiqueta_informacion(self):
        """Creates the labels that describe each info"""
        self.etiqueta_mario = []
        self.etiqueta_mundo = []
        self.etiqueta_tiempo = []
        self.etiqueta_escenario = []


        self.create_etiqueta(self.etiqueta_mario, 'MARIO', 75, 30)
        self.create_etiqueta(self.etiqueta_mundo, 'MUNDO', 450, 30)
        self.create_etiqueta(self.etiqueta_tiempo, 'TIEMPO', 625, 30)
        self.create_etiqueta(self.etiqueta_escenario, '1-1', 472, 55)

        self.lista_etiqueta = [self.etiqueta_mario,
                           self.etiqueta_mundo,
                           self.etiqueta_tiempo,
                           self.etiqueta_escenario]


    def create_etiqueta_pantalla_carga(self):
        """Crea etiquetas para la informacion central de la pantalla de carga"""
        etiqueta_mundo = []
        etiqueta_numero = []

        self.create_etiqueta(etiqueta_mundo, 'MUNDO', 280, 200)
        self.create_etiqueta(etiqueta_numero, '1-1', 430, 200)

        self.etiqueta_central = [etiqueta_mundo, etiqueta_numero]


    def create_reloj_cuentatras(self):
        """Crea el reloj de cuenta atras para el nivel"""
        self.imagen_cuentatras = []
        self.create_etiqueta(self.imagen_cuentatras, str(self.tiempo), 645, 55)


    def create_etiqueta(self, lista_etiqueta, string, x, y):
        """Crea la etiqueta (MUNDO, TIEMPO, MARIO)"""
        for letras in string:
            lista_etiqueta.append(Personaje(self.imagen_dict[letras]))

        self.establece_etiqueta_rects(lista_etiqueta, x, y)


    def establece_etiqueta_rects(self, lista_etiqueta, x, y):
        """Establece la ubicacion de cada caracter individual"""
        for i, letras in enumerate(lista_etiqueta):
            letras.rect.x = x + ((letras.rect.ancho + 3) * i)
            letras.rect.y = y
            if letras.imagen == self.imagen_dict['-']:
                letras.rect.y += 7
                letras.rect.x += 2


    def create_contador_monedas(self):
        """Crea la informacion de la cantidad de monedas que recolecta Mario"""
        self.imagen_contador_monedas = []
        self.create_etiqueta(self.imagen_contador_monedas, '*00', 300, 55)


    def create_efecto_moneda(self):
        """Crea el efecto de la moneda parpadeante """
        self.efecto_moneda = efecto_moneda.Moneda(280, 53)


    def create_mario_imagen(self):
        """LLama a la imagen de MARIO"""
        self.imagen_tiempo_vida = self.get_imagen(75, 247, 6, 6)
        self.tiempo_vida_rect = self.imagen_tiempo_vida.get_rect(center=(378, 295))
        self.etiqueta_total_vidas = []
        self.create_etiqueta(self.etiqueta_total_vidas, str(self.total_vidas),
                          450, 285)

        self.sprite_sheet = configuracion.GFX['mario_bros']
        self.imagen_mario = self.get_imagen(178, 32, 12, 16)
        self.mario_rect = self.imagen_mario.get_rect(center=(320, 290))


    def create_etiqueta_juego_terminado(self):
        """Crea la etiqueta de juego terminado en la pantalla"""
        etiqueta_juego = []
        etiqueta_terminado = []

        self.create_etiqueta(etiqueta_juego, 'JUEGO', 280, 300)
        self.create_etiqueta(etiqueta_terminado, 'TERMINADO', 400, 300)

        self.etiqueta_juego_terminado = [etiqueta_juego, etiqueta_terminado]


    def create_etiqueta_tiempo_terminado(self):
        """Crea una etiqueta de tiempo terminado"""
        etiqueta_tiempo_terminado = []

        self.create_etiqueta(etiqueta_tiempo_terminado, 'TIEMPO TERMINADO', 290, 310)
        self.etiqueta_tiempo_terminado = [etiqueta_tiempo_terminado]


    def create_etiqueta_menu_principal(self):
        """Crea una etiqueta del menu principal en la pantalla"""
        juego_player_one = []
        juego_player_two = []
        top = []
        mejor_puntaje = []

        self.create_etiqueta(juego_player_one, '1 JUGADOR', 272, 360)
        self.create_etiqueta(juego_player_two, '2 JUGADORES', 272, 405)
        self.create_etiqueta(top, 'MEJOR PUNTAJE - ', 290, 465)
        self.create_etiqueta(mejor_puntaje, '000000', 400, 465)

        self.etiqueta_menu_principal = [juego_player_one, juego_player_two,
                                 top, mejor_puntaje]


    def actualiza(self, informacion_nivel, mario=None):
        """Actualiza toda la informacion general"""
        self.mario = mario
        self.manejo_estado_nivel(informacion_nivel)


    def manejo_estado_nivel(self, informacion_nivel):
        """Actualiza la informacion dependiendo del estado en que se encuentre el juego"""
        if self.estado == c.MENU_PRINCIPAL:
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            self.actualiza_imagen_puntaje(self.etiqueta_menu_principal[3], self.mejor_puntaje)
            self.actualiza_total_monedas(informacion_nivel)
            self.efecto_moneda.actualiza(informacion_nivel[c.TIEMPO_ACTUAL])

        elif self.estado == c.PANTALLA_CARGA:
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            self.actualiza_total_monedas(informacion_nivel)

        elif self.estado == c.NIVEL:
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            if informacion_nivel[c.ESTADO_NIVEL] != c.FREEZADO \
                    and self.mario.estado != c.CAMINANDO_AL_CASTILLO \
                    and self.mario.estado != c.CAIDA_DEL_TERRENO \
                    and not self.mario.muerto:
                self.actualiza_reloj_cuentatras(informacion_nivel)
            self.actualiza_total_monedas(informacion_nivel)
            self.efecto_moneda.actualiza(informacion_nivel[c.TIEMPO_ACTUAL])

        elif self.estado == c.TIEMPO_TERMINADO:
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            self.actualiza_total_monedas(informacion_nivel)

        elif self.estado == c.JUEGO_TERMINADO:
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            self.actualiza_total_monedas(informacion_nivel)

        elif self.estado == c.CUENTATRAS_RAPIDA:
            informacion_nivel[c.PUNTAJE] += 50
            self.puntaje = informacion_nivel[c.PUNTAJE]
            self.actualiza_reloj_cuentatras(informacion_nivel)
            self.actualiza_imagen_puntaje(self.imagen_puntaje, self.puntaje)
            self.actualiza_total_monedas(informacion_nivel)
            self.efecto_moneda.actualiza(informacion_nivel[c.TIEMPO_ACTUAL])
            if self.tiempo == 0:
                self.estado = c.FIN_DEL_NIVEL

        elif self.estado == c.FIN_DEL_NIVEL:
            self.efecto_moneda.actualiza(informacion_nivel[c.TIEMPO_ACTUAL])


    def actualiza_imagen_puntaje(self, imagen, puntaje):
        """Actualiza que numeros se deben borrar para el puntaje"""
        indice = len(imagen) - 1

        for digito in reversed(str(puntaje)):
            rect = imagen[indice].rect
            imagen[indice] = Personaje(self.imagen_dict[digito])
            imagen[indice].rect = rect
            indice -= 1


    def actualiza_reloj_cuentatras(self, informacion_nivel):
        """Actualiza el tiempo actual"""
        if self.estado == c.CUENTATRAS_RAPIDA:
            self.tiempo -= 1

        elif (informacion_nivel[c.TIEMPO_ACTUAL] - self.tiempo_actual) > 400:
            self.tiempo_actual = informacion_nivel[c.TIEMPO_ACTUAL]
            self.tiempo -= 1
        self.imagen_cuentatras = []
        self.create_etiqueta(self.imagen_cuentatras, str(self.tiempo), 645, 55)
        if len(self.imagen_cuentatras) < 2:
            for i in range(2):
                self.imagen_cuentatras.insert(0, Personaje(self.imagen_dict['0']))
            self.establece_etiqueta_rects(self.imagen_cuentatras, 645, 55)
        elif len(self.imagen_cuentatras) < 3:
            self.imagen_cuentatras.insert(0, Personaje(self.imagen_dict['0']))
            self.establece_etiqueta_rects(self.imagen_cuentatras, 645, 55)


    def actualiza_total_monedas(self, informacion_nivel):
        """Actualiza la cantidad de monedas y ajusta la etiqueta"""
        self.total_monedas = informacion_nivel[c.TOTAL_MONEDAS]

        cadena_moneda = str(self.total_monedas)
        if len(cadena_moneda) < 2:
            cadena_moneda = '*0' + cadena_moneda
        elif len(cadena_moneda) > 2:
            cadena_moneda = '*00'
        else:
            cadena_moneda = '*' + cadena_moneda

        x = self.imagen_contador_monedas[0].rect.x
        y = self.imagen_contador_monedas[0].rect.y

        self.imagen_contador_monedas = []

        self.create_etiqueta(self.imagen_contador_monedas, cadena_moneda, x, y)
    

    def dibuja(self, surface):
        """Dibuja información general basada en el estado"""
        if self.estado == c.MENU_PRINCIPAL:
            self.dibuja_info_menu_prin(surface)
        elif self.estado == c.PANTALLA_DE_CARGA:
            self.dibuja_info_pantalla_carga(surface)
        elif self.estado == c.NIVEL:
            self.dibuja_info_nivel_pantalla(surface)
        elif self.estado == c.JUEGO_TERMINADO:
            self.dibuja_info_juego_terminado_pant(surface)
        elif self.estado == c.CUENTA_REGRESIVA_RAPIDA:
            self.dibuja_info_nivel_pantalla(surface)
        elif self.estado == c.FINAL_DEL_NIVEL:
            self.dibuja_info_nivel_pantalla(surface)
        elif self.estado == c.TIEMPO_TERMINADO:
            self.dibuja_info_tiempo_terminado_pant(surface)
        else:
            pass



    def dibuja_info_menu_prin(self, surface):
        """Dibuja información para el menú principal"""
        for info in self.imagen_puntaje:
            surface.blit(info.image, info.rect)

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for character in self.imagen_contador_monedas:
            surface.blit(character.image, character.rect)

        for label in self.lista_etiqueta:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.efecto_moneda.image, self.efecto_moneda.rect)


    def dibuja_info_pantalla_carga(self, surface):
        """Dibuja información para la pantalla de carga"""
        for info in self.imagen_puntaje:
            surface.blit(info.image, info.rect)

        for word in self.etiqueta_central:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.etiqueta_total_vidas:
            surface.blit(word.image, word.rect)

        surface.blit(self.mario_image, self.mario_rect)
        surface.blit(self.imagen_tiempo_vida, self.life_times_rect)

        for character in self.imagen_contador_monedas:
            surface.blit(character.image, character.rect)

        for label in self.lista_etiqueta:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.efecto_moneda.image, self.efecto_moneda.rect)


    def dibuja_info_nivel_pantalla(self, surface):
        """Dibuja información durante el juego regular"""
        for info in self.imagen_puntaje:
            surface.blit(info.image, info.rect)

        for digit in self.imagen_cuentatras:
                surface.blit(digit.image, digit.rect)

        for character in self.imagen_contador_monedas:
            surface.blit(character.image, character.rect)

        for label in self.lista_etiqueta:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.efecto_moneda.image, self.efecto_moneda.rect)


    def dibujar_info_juego_terminado_pant(self, surface):
        """Dibuja información cuando termina el juego"""
        for info in self.imagen_puntaje:
            surface.blit(info.image, info.rect)

        for word in self.etiqueta_juego_terminado:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.imagen_contador_monedas:
            surface.blit(character.image, character.rect)

        for label in self.lista_etiqueta:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.efecto_moneda.image, self.efecto_moneda.rect)


    def dibuja_info_tiempo_terminado_pant(self, surface):
        """Extrae información cuando está en la pantalla de tiempo de espera"""
        for info in self.imagen_puntaje:
            surface.blit(info.image, info.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.imagen_contador_monedas:
            surface.blit(character.image, character.rect)

        for label in self.lista_etiqueta:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.efecto_moneda.image, self.efecto_moneda.rect)












