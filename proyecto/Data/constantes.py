ANCHO_PANTALLA = 600
ALTO_PANTALLA = 800
TAMAÑO_PANTALLA = (ANCHO_PANTALLA,ALTO_PANTALLA)

TITULO_ORIGINAL = "Super Mario Bros - Nivel 1"

#======= COLORES ============# 

#              R    G    B
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
PEQUEÑO_A_GRANDE = 'pequeño a grande'
GRANDE_PARA_DISPARAR = 'grande para disparar'
GRANDE_A_PEQUEÑO = 'grande a pequeño'
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