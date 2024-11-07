import pygame
import os
import imagenes
import jugador

pygame.init()
width = 1000
height = 700

#tamaño d ventana
screen = pygame.display.set_mode((width, height))

#nombre de ventana
pygame.display.set_caption("juego de prueba")

pepe = jugador.player()

#actualizar animacion
last_update = pygame.time.get_ticks()
animation_coldown = 300
frame = 0
#color pantalla
color = 70, 170, 200
#empezar bucle
run = True
while run:
    #ponemos los eventos q ocurren
    for event in pygame.event.get():
        #si es salir de la ventana terminamos
        if event.type == pygame.QUIT: run = False
    
    pepe.caminar = False
    aceleracion = 5
    
    #colición
    keys = pygame.key.get_pressed() 
    # 40 es la cantidad de pixeles que hay entre el sprite y los bordes de colición
    if keys[pygame.K_UP] and pepe.imagenrect.top > -40:
        #pepe.imagenrect = pepe.imagenrect.move(0,-1)
        pepe.movimiento_y = -1
        pepe.cambiar_direccion(1)
        pepe.caminar = True

    if keys[pygame.K_DOWN] and pepe.imagenrect.bottom < height + 40:
        #pepe.imagenrect = pepe.imagenrect.move(0,1)
        pepe.movimiento_y = 1
        pepe.cambiar_direccion(0)
        pepe.caminar = True

         
    if keys[pygame.K_RIGHT] and pepe.imagenrect.right < width + 40:
        #pepe.imagenrect = pepe.imagenrect.move(1,0)
        pepe.movimiento_x = 1
        pepe.cambiar_direccion(3)
        pepe.caminar = True
        
    if keys[pygame.K_LEFT] and pepe.imagenrect.left > -40:
        #pepe.imagenrect = pepe.imagenrect.move(-1,0)
        pepe.movimiento_x = -1
        pepe.cambiar_direccion(2)
        pepe.caminar = True

    #jugador corre y animación acelera
    if keys[pygame.K_SPACE]:
        aceleracion = 2
        animation_coldown = 150
    else:
        animation_coldown = 300
     
 
    
    if pepe.movimiento_x != 0 or pepe.movimiento_y != 0:
    #actualizar movmiento
        pepe.imagenrect = pepe.imagenrect.move(pepe.movimiento_x, pepe.movimiento_y)
        pepe.movimiento_x = 0
        pepe.movimiento_y = 0
        
        #delay al movimiento del personaje
        pygame.time.delay(aceleracion)
    
    screen.fill(color)
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_coldown:
        frame += 1
        frame = frame % 2
        last_update = current_time
        
    if pepe.caminar:
        screen.blit(pepe.animation_list_walk[frame], pepe.imagenrect)
    else:
        screen.blit(pepe.animation_list_idle[frame], pepe.imagenrect)
    pygame.display.flip()
pygame.QUIT