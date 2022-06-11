ANCHO_PANTALLA = 600
ALTO_PANTALLA = 800
TAMAÑO_PANTALLA = (ANCHO_PANTALLA,ALTO_PANTALLA)

TITULO_ORIGINAL = "Super Mario Bros - Nivel 1"

#======= COLORES ============# 

#                  R    G    B
GRIS           = (100, 100, 100)
AZULMARINO     = ( 60,  60, 100)
BLANCO         = (255, 255, 255)
ROJO           = (255,   0,   0)
VERDE          = (  0, 255,   0)
VERDE_BOSQUE   = ( 31, 162,  35)
AZUL           = (  0,   0, 255)
CIELO_AZUL     = ( 39, 145, 251)
AMARILLO       = (255, 255,   0)
NARANJA        = (255, 128,   0)
VIOLETA        = (255,   0, 255)
CELESTE        = (  0, 255, 255)
NEGRO          = (  0,   0,   0)
GRIS_OSCURO    = ( 19,  15,  48)
CELESTE_CLARO  = (233, 232, 255)
DORADO         = (255, 215,   0)

COLOR_DE_FONTO = BLANCO

TAMAÑO_MULTIPLICADOR = 2.5
TAMAÑO_BLOQUE_MULTIPLICADOR = 2.69
MULTIPLICADOR_DE_FONDO = 2.679
ALTURA_DE_SUELO= ALTO_PANTALLA - 62

#========FUERZAS ACTUANTES EN MARIO==========#
ACELERACION_CAMINAR = .15
MAXIMA_VELOCIDAD_CAMINAR = 6

MAXIMA_VELOCIDAD_CORRER = 800
ACELERACION_CORRER = 20

GIRO_PEQUEÑO = .35

GRAVEDAD = 1.01
GRAVEDAD_DE_SALTO = .31

VELOCIDAD_DE_SALTO = -12
VELOCIDAD_SALTO_RAPIDO = -12.5

MAX_VEL_EJEY = 11



#Estados de mario

PARARSE = 'de pie'
CAMINAR = 'caminar'
SALTO = 'salto'
CAERSE = 'caerse'
PEQUENIO_A_GRANDE = 'pequenio a grande'
GRANDE_PARA_DISPARAR = 'grande para disparar'
GRANDE_A_PEQUENIO = 'grande a pequenio'
ASTA_DE_BANDERA = 'asta de bandera'
CAMINANDO_AL_CASTILLO = 'caminando al castillo'
FIN_DEL_NIVEL = 'fin del nivel'


#Cosas de GOOMBA

IZQUIERDA = 'izquierda'
DERECHA = 'derecha'
SALTO_SOBRE = 'salto sobre'
SALTO_MORTAL = 'salto mortal'

#Cosas de KOOPA

DESLICE_DE_CAPARAZON = 'deslice_de_caparazon'

#Estados del ladrillo

LADRILLO_EN_REPOSO = 'ladrillo en reposo'
LADRILLO_GOLPEADO = 'ladrillo golpeado'

#Estados de la moneda
ABIERTA = 'abierta'

#Estados del hongo

REVELADO = 'revelado'
DESLIZANDOSE = 'deslizandose'

#Estados de la moneda

GIRAR = 'girar'

#Estados de las estrellas

REBOTE = 'rebote'

#Estados del fuego

VOLANDO = 'VOLANDO'
REBOTANDO = 'rebotando'
EXPLOTANDO = 'explotando'

#Contenidos de las cajas y monedas

HONGOS = 'hongos'
ESTRELLA = 'estrella'
FLOR_FUEGO = 'flordefuego'
SEISMONEDAS = '6monedas'
MONEDA = 'moneda'
HONGO_DE_VIDA = 'vida_extra_hongo'

BOLA_DE_FUEGO = 'boladefuego'

#Listado de Enemigos

GOOMBA = 'goomba' # el honguito marron
KOOPA = 'koopa'   # La tortuga

#Estados de los niveles

CONGELADO = 'congelado'
NO_CONGELADO = 'no congelado'
EN_CASTILLO = 'en castillo'
BANDERA_Y_FUEGOS_ARTIFICIALES = 'bandera y fuegos artificiales'

#Estado de la bandera
ARRIBA_MASTIL = 'arriba del mastil'
MEDIO_MASTIL = 'medio del mastil'
BAJO_MASTIL = 'parte de abajo del mastil'

#puntaje para la vida extra
UNA_VIDA = '379'

#OPCIONES DEL CURSOR DEL MENU PRINCIPAL
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#Estado de informacion en la parte superior
MENU_PRINCIPAL = 'menu principal'
PANTALLA_DE_CARGA = 'pantalla de carga'
NIVEL = 'nivel'
JUEGO_TERMINADO = 'juego terminado'
CUENTA_REGRESIVA_RAPIDA = 'cuenta regresiva rapida'
FINAL_DEL_NIVEL = 'final del nivel'


#Info de las teclas del juego
TOTAL_MONEDAS = 'total de monedas'
PUNTAJE = 'puntaje'
MEJOR_PUNTAJE = 'mejor puntaje'
VIDAS = 'vidas'
TIEMPO_ACTUAL = 'tiempo actual'
ESTADO_DEL_NIVEL = 'estado del nivel'
INICIO_DE_CAMARA_X = 'inicio de la camara x'
MARIO_MUERTO = 'mario muerto'

#ESTADOS PARA TODO EL JUEGO
MENU_PRINCIPAL = 'menu principal'
PANTALLA_DE_CARGA = 'pantalla de carga'
TIEMPO_TERMINADO = 'tiempo terminado'
JUEGO_TERMINADO = 'juego terminado'
NIVEL1 = 'nivel 1'

#ESTADOS DE SONIDOS
NORMAL = 'normal'
NIVEL_TERMINADO = 'nivel terminado'
MUNDO_TERMINADO = 'mundo terminado'
AVISO_DE_TIEMPO = 'aviso de poco tiempo restante'
VELOCIDAD_NORMAL = 'velocidad normal'
MARIO_INVENCIBLE = 'mario invencible'