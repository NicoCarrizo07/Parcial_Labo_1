import pygame
#import random
#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
CYAN = (0,255,255)
colores = [RED,WHITE,GREEN,BLUE,CYAN,YELLOW]

#tamanio  W,H w=ancho h= alto
WIDTH = 800
HEIGHT = 600
SIZE_SCREEN = (WIDTH, HEIGHT)
FPS = 60
CENTER_SCREEN = (WIDTH//2,HEIGHT//2) #para el circulo el medio es la mitad del width y height
SPEED = 5

#direcciones
UR = 9
DR = 3
DL = 1
UL =7

#Bloque
BLOCK_WIDTH = 130
BLOCK_HEIGHT = 130
speed_x = 5
speed_y = 5

#Configuraciones enemigos
size_enemigo = 30
size_min_enemigo = 55
size_max_enemigo= 65
speed_min_enemigo = 1
speed_max_enemigo = 2
count_enemigos = 10
cont_grande = 0

#Lazer
sise_disparo = (50,100) #2,5
speed_disparo = 6

#Botones
buttom_width = 200
buttom_height = 50

buttom_comenzar = pygame.Rect(0,0,buttom_width,buttom_height)
buttom_comenzar.center = (CENTER_SCREEN)

button_salir = pygame.Rect(0, 0, buttom_width, buttom_height)
button_salir.center = (CENTER_SCREEN[0], CENTER_SCREEN[1] + buttom_height + 20)

buttom_instrucciones = pygame.Rect(0,0,buttom_width,buttom_height)
buttom_instrucciones.center = (CENTER_SCREEN[0], CENTER_SCREEN[1] + 2 * buttom_height + 40)

#Trucos
trick_reverse = False
trick_slow = False

#direccion movimiento tecla
move_up =False
move_right =False
move_down =False
move_left =False

max_score = 0
disparo = None

segunda_oleada = False
bonus_agarrado = False


level1_pass = True

#cargar imagenes
image_player = pygame.image.load(r"Parcial Entrega\Imagenes\messi png.png")
image_ronaldo = pygame.image.load(r"Parcial Entrega\Imagenes\ronaldo1-removebg-preview.png")
fondo = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\barca.jpg"),SIZE_SCREEN)
imagen_mbape = pygame.image.load(r"Parcial Entrega\Imagenes\mbape-removebg-preview.png")
imagen_copa = pygame.image.load(r"Parcial Entrega\Imagenes\copa-removebg-preview.png")
disparo_mask = pygame.mask.from_surface(imagen_copa)
enemigo_mask = pygame.mask.from_surface(image_ronaldo)
imagen_parlante = pygame.image.load(r"Parcial Entrega\Imagenes\parlantito-removebg-preview.png")
imagen_parlante_reescalada = pygame.transform.scale(imagen_parlante, (70, 70))
fondo_psg = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\estadio psg.jpg"),SIZE_SCREEN)
fondo_victoria = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\qatar-2022-messi-besa-copa-del-mundo-770x470.jpg"),SIZE_SCREEN)
imagen_nivel1_pasado = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\messi_ronaldo.jpg"),SIZE_SCREEN)
imagen_principio = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\messi_copa.jpg"),SIZE_SCREEN)
imagen_messi_llorando = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\messi_llorando.jpg"),SIZE_SCREEN)
imagen_balon_oro = pygame.image.load(r"Parcial Entrega\Imagenes\balon de oro.png")
imagen_instrucciones = pygame.transform.scale(pygame.image.load(r"Parcial Entrega\Imagenes\messi instrucciones.jpg"),SIZE_SCREEN)
imagen_visible_parlante = False
imagen_pepsi = pygame.image.load(r"Parcial Entrega\Imagenes\pepsi.png")

