
from .import configuracion,herramientas
from .Estados import menu_principal,pantalla_de_carga,nivel1
from . import constantes as c


def main():
    """Agregar estados de control."""
    correr_eso = herramientas.Control(configuracion.ORIGINAL_CAPTION)
    estado_diccionaro = {c.MENU_PRINCIPAL: menu_principal.Menu(),
                  c.PANTALLA_DE_CARGA: pantalla_de_carga.PantallaDeCarga(),
                  c.TIEMPO_TERMINADO: pantalla_de_carga.TiempoTerminado(),
                  c.JUEGO_TERMINADO: pantalla_de_carga.JuegoTerminado(),
                  c.NIVEL1: nivel1.Nivel1()}

    correr_eso.estado_configuracion(estado_diccionaro, c.MENU_PRINCIPAL)
    correr_eso.main()



