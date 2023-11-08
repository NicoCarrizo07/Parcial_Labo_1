import pygame
import sys
from configuraciones import *
from random import *
from colisiones import *
from pygame.locals import *
from funciones import *

SCREEN = pygame.display.set_mode(SIZE_SCREEN)  # displey crear pantalla

def wait_user_clik_comenzar(rect_comenzar:pygame.Rect,rect_salir:pygame.Rect,rect_instrucciones:pygame.Rect):
    """Pausar el juego hasta que el jugador haga clik en pantalla

    Args:
        rect_comenzar: rectangulo donde si haces clik el juego comienza
        rect_salir: rectangulo donde si haces clik el juego muestra los comandos
        rect_instrucciones : rectangulo donde si haces clik el juego comienza finaliza

    Returns:
        None
    """
    while True:
        crear_boton(SCREEN,rect_comenzar,"Comenzar",BLUE,RED)
        crear_boton(SCREEN,rect_instrucciones,"Comandos",BLUE,RED)
        crear_boton(SCREEN,rect_salir,"Salir",BLUE,RED)
        pygame.display.flip() #PINTAR PANTALLA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == KEYDOWN: #evento presionar tecla
                if event.key == K_ESCAPE:
                    terminar()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_comenzar.collidepoint(event.pos):
                        click_sound.play()
                        return None
                    elif rect_salir.collidepoint(event.pos):
                        click_sound.play()
                        terminar()
                    elif rect_instrucciones.collidepoint(event.pos):
                        click_sound.play()
                        SCREEN.blit(imagen_instrucciones, (0,0))
                        pygame.display.flip() #PINTAR PANTALLA
                        wait_user()
                        return None

pygame.init()  #inicializar pygame

#Nombre del juego
pygame.display.set_caption("Jueguito Parcial Labo I")

#FUENTE
fuente = pygame.font.SysFont(None,50)#(fuente,tamanio)crear obejeto de la clase fuente
contador = 0
texto = fuente.render(f"Score : {contador}",True, WHITE)
rect_texto = texto.get_rect()
rect_texto.midtop = (WIDTH //2 , 30)

block = crear_bloque(image_player,300,
        480,BLOCK_WIDTH , BLOCK_HEIGHT,
        RED,radio = 25)

bonus = crear_bloque(imagen_pepsi,randint(0, WIDTH - 50),
    -50,25 , 50,
    RED,radio = 25, speed_y=1)


def dibujar_enemigos(superficie,enemigos):
    """Dibuja los enemigos en pantalla

    Args:
        superficie: lugar donde dibujarlos (pantalla)
        enemigos: lista de enemigos a dibujar en pantalla


    Returns:
        None
    """
    for enemigo in enemigos:
        if enemigo["img"]:
            superficie.blit(enemigo["img"],enemigo["rect"])
        else:
            pygame.draw.rect(superficie,enemigo["color"],enemigo["rect"],enemigo["borde"],enemigo["radio"])

clock = pygame.time.Clock() #clase clock

#set sonido
colision_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\X2Download.app - SOUND OFF ROBLOX SONIDO OFF MUERTE DE ROBLOX (128 kbps).mp3")
winner_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\success-fanfare-trumpets-6185.mp3")
pygame.mixer.music.load(r"Parcial Entrega\Sonidos\La T y La M - Pa la Selección (Video Oficial).mp3")
bobo_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\Y2meta.app - Messi-s _¿Que miras bobo__ Sound Effect (128 kbps).mp3")
pygame.mixer.music.set_volume(0.1)
game_over_sound =  pygame.mixer.Sound(r"Parcial Entrega\Sonidos\081790_quotgame-overquot-evil-88883.mp3")
click_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\mouse-click-153941.mp3")
bonus_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\Sonido Mario Bros -  1up (vida extra) (128 kbps).mp3")
victoria_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\SaveTube.App - Victory - Sound Effect (128 kbps).mp3")
disparo_sound = pygame.mixer.Sound(r"Parcial Entrega\Sonidos\hq-explosion-6288 (mp3cut.net).mp3")
playing_music = True

try:
    with open('max_score.txt', 'r') as file:
        max_score = int(file.read())
except:
    max_score = 0

try:
    with open('ultimo_score.txt', 'r') as file:
        contador = int(file.read())
except:
    contador = 0


while True:

    #pantalla inicio
    SCREEN.blit(imagen_principio, (0,0))
    mostrar_texto(SCREEN,"Messi Game",fuente,(WIDTH//2,20),RED,BLUE) #WIDTH//2 mitad  de la pantalla
    mostrar_texto(SCREEN,"Nivel 1",fuente,(WIDTH//2,70),RED,BLUE) #WIDTH//2 mitad  de la pantalla
    mostrar_texto(SCREEN,f"Last score : {contador}",fuente,(WIDTH//2,HEIGHT-68),YELLOW)
    mostrar_texto(SCREEN,f"Max score : {max_score}",fuente,(WIDTH//2,HEIGHT - 30),YELLOW)
    wait_user_clik_comenzar(buttom_comenzar,buttom_instrucciones,button_salir)
    level1_pass == True
    print(level1_pass)
    #Inicio juego
    vidas = 3
    contador = 0
    texto = fuente.render(f"Score : {contador}",True, WHITE)
    rect_texto = texto.get_rect(topleft=(30, 40))

    texto_vidas = fuente.render(f"Vidas : {vidas}",True, WHITE)
    rect_texto_vidas = texto_vidas.get_rect(topright=(WIDTH-30, 40))

    tiempo_juego = FPS * 60
    is_running =True
    pygame.mixer.music.play(0)

    enemigos = []
    disparos = []
    bonuss = []
    bonuss.append(bonus)
    rafaga = True
    load_enemigos_list(enemigos,count_enemigos,image_ronaldo)    

    while is_running:
        level1_pass == True
        clock.tick(FPS) #regular velocidad del while(60 iteraciones por segundo) 
        tiempo_juego -= 1
        for event in pygame.event.get():  #lista de eventos a detectar/analizar
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == KEYDOWN: #evento presionar tecla
                if event.key == K_f:
                    #disparo_sound.play()
                    if segunda_oleada == False:
                        if rafaga:
                            midtop = block["rect"].midtop
                            disparo_w , disparo_h = sise_disparo
                            disparos.append(crear_bloque(imagen_copa,midtop[0] - disparo_w//2,
                            midtop[1] - disparo_h,disparo_w,disparo_h,RED,speed_y=speed_disparo)) #none cambiar por imagen copa) 
                        else:
                            if not disparo:
                                midtop = block["rect"].midtop
                                disparo_w , disparo_h = sise_disparo
                                disparo = crear_bloque(imagen_copa,midtop[0] - disparo_w//2,
                                midtop[1] - disparo_h,disparo_w,disparo_h,RED,speed_y=speed_disparo) #none cambiar por imagen copa
                    elif segunda_oleada == True:
                        if rafaga:
                            midtop = block["rect"].midtop
                            sise_disparo = (55,55)
                            disparo_w , disparo_h = sise_disparo
                            disparos.append(crear_bloque(imagen_balon_oro,midtop[0] - disparo_w//2,
                            midtop[1] - disparo_h,disparo_w,disparo_h,RED,speed_y=speed_disparo)) #none cambiar por imagen copa) 
                        else:
                            if not disparo:
                                midtop = block["rect"].midtop
                                sise_disparo = (55,55)
                                disparo_w , disparo_h = sise_disparo
                                disparo = crear_bloque(imagen_balon_oro,midtop[0] - disparo_w//2,
                                midtop[1] - disparo_h,disparo_w,disparo_h,RED,speed_y=speed_disparo) #none cambiar por imagen copa

                if event.key == K_RIGHT or event.key == K_d:
                    move_right = True
                    move_left = False
                
                elif event.key == K_LEFT or event.key == K_a:
                    move_left = True
                    move_right = False

                if event.key == K_m:
                    imagen_visible_parlante = not imagen_visible_parlante
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                    playing_music = not playing_music

                if event.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                    mostrar_texto(SCREEN,"Pausa",fuente,CENTER_SCREEN,RED,BLUE)
                    pygame.display.flip()
                    wait_user()
                    
                    if playing_music:
                        pygame.mixer.music.unpause()
                
                if event.key == K_r:
                    trick_reverse = True

                if event.key == K_l:
                    trick_slow = True
                
                if event.key == K_l:
                    rafaga = not rafaga

            if event.type == KEYUP: #cuando suelto la tecla cambia la bandera
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                
                elif event.key == K_LEFT or event.key == K_a:
                    move_left = False

                elif event.key == K_ESCAPE:
                    is_running = False

                elif event.key == K_r:
                    trick_reverse = False

                elif event.key == K_l:
                    trick_slow = False

        #------> actualizar los elementos
        
        #muevo el personaje
        #si se mueve a la derecha que choque y no se me vaya de pantalla
        if move_right and block["rect"].right <= (WIDTH - (SPEED-20)):
            block["rect"].left += SPEED 
        
        #si se mueve a la izquierda que choque y no se me vaya de pantalla
        if move_left and block["rect"].left >= (0 + (SPEED-20)): 
            block["rect"].left -= SPEED 

        #mover disparo
        if rafaga:
            for disparo in disparos[:]:
                if disparo["rect"].bottom > 0:
                    disparo["rect"].move_ip(0,-disparo["speed_y"])
                else:
                    disparos.remove(disparo)
        else:
            if disparo:
                if disparo["rect"].bottom > 0:
                    disparo["rect"].move_ip(0,-disparo["speed_y"])
                else: 
                    disparo = None

        #Mover bonus
        bonus["rect"].move_ip(0,bonus["speed_y"])

        # Volver a aparecer el bonus en la parte superior cuando llegue al fondo
        if bonus["rect"].top > HEIGHT:
            bonus["rect"].top = -50
            bonus["rect"].left = randint(0, WIDTH - 50)     

        for bonus in bonuss[:]:
            if detectar_colision(block["rect"], bonus["rect"]):
                bonuss.remove(bonus)
                bonus_sound.play()
                if vidas > 1:
                    vidas +=1
                    texto_vidas = fuente.render(f"Vidas : {vidas}",True, WHITE)
                    rect_texto_vidas = texto_vidas.get_rect(topright=(WIDTH-30, 40))
                bonus_agarrado = True

        #MOVER ENEMIGOS
        for enemigo in enemigos:
            if not trick_reverse and not trick_slow: 
                enemigo["rect"].move_ip(0,enemigo["speed_y"])
            elif trick_reverse == True:
                enemigo["rect"].move_ip(0,-enemigo["speed_y"])
            elif trick_slow == True:
                enemigo["rect"].move_ip(0,1)

        #volver a aparecer ENEMIGOS desde arriba
        for enemigo in enemigos[:]:
            if enemigo["rect"].top > HEIGHT:
                #enemigos.remove(enemigo)
                enemigo["rect"].y = - enemigo["rect"].height

        for enemigo in enemigos[ : ]: #lista paralela copiada q no modifica la original
            if detectar_colision(enemigo["rect"], block["rect"]):
                enemigos.remove(enemigo)
                if vidas > 1:
                    vidas -=1
                    texto_vidas = fuente.render(f"Vidas : {vidas}",True, WHITE)
                    rect_texto_vidas = texto_vidas.get_rect(topright=(WIDTH-30, 40))
                else:
                    is_running = False

                if playing_music: 
                    colision_sound.play()

                if contador ==20:
                    victoria_sound.play()
                    SCREEN.blit(fondo_victoria, (0,0))
                    mostrar_texto(SCREEN,"Ayudaste a Messi a ser campeon mundial",fuente,(WIDTH//2,250),WHITE)
                    mostrar_texto(SCREEN,"Felicitaciones, juego completado !!!!!",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                    mostrar_texto(SCREEN,f"Su puntuacion fue : {contador}",fuente,(WIDTH//2,HEIGHT - 30),YELLOW)
                    pygame.display.flip()
                    wait_user()
                    terminar()

                if len(enemigos) == 0:
                    #bonus_agarrado = False
                    segunda_oleada = True
                    if level1_pass == True:
                        print("entre")
                        winner_sound.play()
                        SCREEN.blit(imagen_nivel1_pasado, (0,0))
                        mostrar_texto(SCREEN,"Nivel 2",fuente,(WIDTH//2,20),BLUE) #WIDTH//2 mitad  de la pantalla
                        mostrar_texto(SCREEN,"Has derrotado a CR7!",fuente,(WIDTH//2,250),WHITE)
                        mostrar_texto(SCREEN,"Precione una tecla para pasar de nivel",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                        pygame.display.flip()
                        wait_user()
                    else:
                        None
                    SCREEN.blit(fondo_psg, (0,0))
                    load_enemigos_list(enemigos, count_enemigos,imagen_mbape) #segunda oleada de enemigos
                    level1_pass = False

        if rafaga:
            for disparo in disparos[:]:
                colision = False
                for enemigo in enemigos[ : ]: 
                    if detectar_colision(enemigo["rect"], disparo["rect"]):
                        enemigos.remove(enemigo)
                        contador +=1
                        texto = fuente.render(f"Score : {contador}",True, WHITE)
                        rect_texto = texto.get_rect(topleft=(30, 40))
                        colision = True
                        if playing_music: 
                            bobo_sound.play()

                        if contador ==20:
                            victoria_sound.play()
                            SCREEN.blit(fondo_victoria, (0,0))
                            mostrar_texto(SCREEN,"Ayudaste a Messi a ser campeon mundial",fuente,(WIDTH//2,250),WHITE)
                            mostrar_texto(SCREEN,"Felicitaciones, juego completado !!!!!",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                            mostrar_texto(SCREEN,f"Su puntuacion fue : {contador}",fuente,(WIDTH//2,HEIGHT - 30),YELLOW)
                            pygame.display.flip()
                            wait_user()
                            terminar()

                        if len(enemigos) == 0:
                            segunda_oleada = True
                            if level1_pass == True:
                                print("entre")
                                winner_sound.play()
                                SCREEN.blit(imagen_nivel1_pasado, (0,0))
                                mostrar_texto(SCREEN,"Nivel 2",fuente,(WIDTH//2,20),BLUE) #WIDTH//2 mitad  de la pantalla
                                mostrar_texto(SCREEN,"Has derrotado a CR7!",fuente,(WIDTH//2,250),WHITE)
                                mostrar_texto(SCREEN,"Precione una tecla para pasar de nivel",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                                pygame.display.flip()
                                wait_user()
                            else:
                                None

                            SCREEN.blit(fondo_psg, (0,0))
                            load_enemigos_list(enemigos, count_enemigos,imagen_mbape) #segunda oleada de enemigos
                            level1_pass = False

                if colision == True:
                    disparos.remove(disparo)

        else:
            if disparo:
                colision = False
                for enemigo in enemigos[ : ]:
                    if detectar_colision(enemigo["rect"], disparo["rect"]):
                        enemigos.remove(enemigo)
                        contador +=1
                        texto = fuente.render(f"Score : {contador}",True, WHITE)
                        rect_texto = texto.get_rect(topleft=(30, 40))
                        colision = True
                        if playing_music: 
                            colision_sound.play()

                        if contador ==20:
                            victoria_sound.play()
                            SCREEN.blit(fondo_victoria, (0,0))
                            mostrar_texto(SCREEN,"Ayudaste a Messi a ser campeon mundial",fuente,(WIDTH//2,250),WHITE)
                            mostrar_texto(SCREEN,"Felicitaciones, juego completado !!!!!",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                            mostrar_texto(SCREEN,f"Su puntuacion fue : {contador}",fuente,(WIDTH//2,HEIGHT - 30),YELLOW)
                            pygame.display.flip()
                            wait_user()
                            terminar()

                        if len(enemigos) == 0:
                            segunda_oleada = True
                            if level1_pass == True:
                                print("entre")
                                winner_sound.play()
                                SCREEN.blit(imagen_nivel1_pasado, (0,0))
                                mostrar_texto(SCREEN,"Nivel 2",fuente,(WIDTH//2,20),BLUE) #WIDTH//2 mitad  de la pantalla
                                mostrar_texto(SCREEN,"Has derrotado a CR7!",fuente,(WIDTH//2,250),WHITE)
                                mostrar_texto(SCREEN,"Precione una tecla para pasar de nivel",fuente,(WIDTH//2,HEIGHT//2),WHITE)
                                pygame.display.flip()
                                wait_user()
                            else:
                                None
                            SCREEN.blit(fondo_psg, (0,0))
                            load_enemigos_list(enemigos, count_enemigos,imagen_mbape) #segunda oleada de enemigos
                            level1_pass = False

                if colision == True:
                    disparo = None

        #------> dibujar pantalla
        #blit : pegar una surface arriba de otra
        if segunda_oleada == False:
            SCREEN.blit(fondo, (0,0))   
        elif segunda_oleada == True:
            SCREEN.blit(fondo_psg, (0,0))   

        dibujar_enemigos(SCREEN,enemigos)
        
        if imagen_visible_parlante:
            SCREEN.blit(imagen_parlante_reescalada,(60, 90))

        if rafaga:
            for disparo in disparos:
                SCREEN.blit(disparo["img"],disparo["rect"])
        else:
            if disparo:
                SCREEN.blit(disparo["img"],disparo["rect"])

        SCREEN.blit(block["img"],block["rect"])
        
        SCREEN.blit(texto,rect_texto)
        SCREEN.blit(texto_vidas,rect_texto_vidas)

        for bonus in bonuss:
            SCREEN.blit(bonus["img"], bonus["rect"])

        #------> actualizar la pantalla
        pygame.display.flip()  # actualizar pantalla

        if tiempo_juego == 0:
            break

        if contador > max_score:
            max_score = contador
        elif contador == 19:
            contador > max_score
            max_score = contador + 1

        with open('max_score.txt', 'w') as file:
            file.write(str(max_score))

        with open('ultimo_score.txt', 'w') as file:
            file.write(str(contador))

    level1_pass == True
    SCREEN.blit(imagen_messi_llorando, (0,0))
    game_over_sound.play()
    pygame.mixer.music.stop()
    mostrar_texto(SCREEN,"Game over",fuente,(WIDTH//2,20),WHITE)
    mostrar_texto(SCREEN,"Hiciste llorar a Messi.",fuente,(WIDTH//2,150),WHITE)
    mostrar_texto(SCREEN,"Precione una tecla para volver a jugar",fuente,(WIDTH//2,HEIGHT//2),WHITE)
    mostrar_texto(SCREEN,f"Su puntuacion fue : {contador}",fuente,(WIDTH//2,HEIGHT - 30),YELLOW)
    pygame.display.flip()
    wait_user()
    segunda_oleada = False
    level1_pass == True
    bonus_agarrado = False
    print(level1_pass)