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

frame = 0
#color pantalla
color = 70, 170, 200

img_start = pygame.image.load("boton_START.PNG").convert_alpha()
img_exit = pygame.image.load("boton_EXIT.PNG").convert_alpha()



#empezar bucle
run = True

while run:
    #ponemos los eventos q ocurren
    for event in pygame.event.get():
        #si es salir de la ventana terminamos
        if event.type == pygame.QUIT: run = False
    
    #movimiento
    keys = pygame.key.get_pressed()
    pepe.movimiento(keys, width, height)

    pepe.actualizar_posicion() 
  
    screen.fill(color)
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= pepe.animation_coldown:
        frame += 1
        frame = frame % 2
        last_update = current_time
        
    if pepe.caminar:
        screen.blit(pepe.animation_list_walk[frame], pepe.imagenrect)
    else:
        screen.blit(pepe.animation_list_idle[frame], pepe.imagenrect)
    pygame.display.flip()
    
pygame.QUIT