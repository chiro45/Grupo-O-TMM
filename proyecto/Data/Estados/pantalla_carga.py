from .. import configuracion, herramientas
from .. import constantes as c
from .. import sonido_juego
from ..Componentes import informacion


class PantallaDeCarga(herramientas._Estado):
    def __init__(self):
        herramientas._Estado.__init__(self)

    def startup(self, tiempo_actual, persistir):
        self.tiempo_inicio = tiempo_actual
        self.persistir = persistir
        self.informacion_juego = self.persistir
        self.proximo = self.set_proximo_estado()

        informacion_estado = self.set_estado_informacion_general()

        self.informacion_general = informacion.OverheadInfo(self.informacion_juego, informacion_estado)
        self.administrador_sonido = sonido_juego.sonidos(self.informacion_general)


    def set_proximo_estado(self):
        """Establece el proximo estado"""
        return c.NIVEL1

    def set_estado_informacion_general(self):
        """Establece el estado para enviar al objeto informacion_general"""
        return c.PANTALLA_DE_CARGA


    def actualizacion(self, superficie, llaves, tiempo_actual):
        """Actualiza la pantalla de carga"""
        if (tiempo_actual - self.tiempo_inicio) < 2400:
            superficie.fill(c.BLACK)
            self.informacion_general.actualizacion(self.informacion_juego)
            self.informacion_general.draw(superficie)

        elif (tiempo_actual - self.tiempo_inicio) < 2600:
            superficie.fill(c.BLACK)

        elif (tiempo_actual - self.tiempo_inicio) < 2635:
            superficie.fill((106, 150, 252))

        else:
            self.done = True




class JuegoTerminado(PantallaDeCarga):
    """Carga la pantalla de Juego Terminado"""
    def __init__(self):
        super(JuegoTerminado, self).__init__()


    def set_proximo_estado(self):
        """Pone el proximo estado"""
        return c.MENU_PRINCIPAL

    def set_estado_informacion_general(self):
        """Establece el estado de informacion general otra vez"""
        return c.JUEGO_TERMINADO

    def actualizacion(self, superficie, llaves, tiempo_actual):
        self.tiempo_actual = tiempo_actual
        self.administrador_sonido.actualizacion(self.persistir, None)

        if (self.tiempo_actual - self.tiempo_inicio) < 7000:
            superficie.fill(c.BLACK)
            self.informacion_general.actualizacion(self.informacion_juego)
            self.informacion_general.draw(superficie)
        elif (self.tiempo_actual - self.tiempo_inicio) < 7200:
            superficie.fill(c.BLACK)
        elif (self.tiempo_actual - self.tiempo_inicio) < 7235:
            superficie.fill((106, 150, 252))
        else:
            self.done = True


class TiempoTerminado(PantallaDeCarga):
    """Carga la pantalla de tiempo terminado"""
    def __init__(self):
        super(TiempoTerminado, self).__init__()

    def set_proximo_estado(self):
        """Establece el proximo estado"""
        if self.persistir[c.VIDAS] == 0:
            return c.JUEGO_TERMINADO
        else:
            return c.PANTALLA_DE_CARGA

    def set_estado_informacion_general(self):
        """Establece el estado y envia la informacion de estado general"""
        return c.TIEMPO_TERMINADO

    def actualizacion(self, superficie, llaves, tiempo_actual):
        self.tiempo_actual = tiempo_actual

        if (self.tiempo_actual - self.tiempo_inicio) < 2400:
            superficie.fill(c.BLACK)
            self.informacion_general.actualizacion(self.informacion_juego)
            self.informacion_general.draw(superficie)
        else:
            self.done = True









