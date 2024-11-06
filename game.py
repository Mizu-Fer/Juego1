import pygame
import os
import imagenes

pygame.init()
width = 1000
height = 700

#tamaño d ventana
screen = pygame.display.set_mode((width, height))

#nombre de ventana
pygame.display.set_caption("juego de prueba")


#transparencia de imagen
black = 0, 0, 0
        
#crear variables
class jugador:
    imagen = pygame.image.load("jugador.png").convert_alpha()
    imagenespepe = imagenes.spritesheet(imagen)    
    
    #animación de imagen
    animation_list_idle = []
    animation_list_walk = []
    animation_steps = 2
    
    #agregar imagenes en las listas de animacion
    for x in range(animation_steps):
        animation_list_idle.append(imagenespepe.get_image( x, 0, 48, 48, 3, black))
    for x in range(animation_steps):
        animation_list_walk.append(imagenespepe.get_image( x + 2, 0, 48, 48, 3, black))
    
    #frame_0 usado como molde xq tienen el mismo tamaño
    imagenrect = animation_list_idle[0].get_rect()
    movimiento_x = 0
    movimiento_y = 0
    def move_forward():
        imagenrect = imagenrect.move(speed)
        
    #sur = 0 , norte
    def cambiar_direccion():
        pass
        

pepe = jugador()
pepe.imagenrect.move_ip(300,100)
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
    
    #colición
    keys = pygame.key.get_pressed() 
    # 40 es la cantidad de pixeles que hay entre el sprite y los bordes de colición
    if keys[pygame.K_UP] and pepe.imagenrect.top > -40:
        #pepe.imagenrect = pepe.imagenrect.move(0,-1)
        pepe.movimiento_y = -1
    if keys[pygame.K_DOWN] and pepe.imagenrect.bottom < height + 40:
        #pepe.imagenrect = pepe.imagenrect.move(0,1)
        pepe.movimiento_y = 1
    if keys[pygame.K_LEFT] and pepe.imagenrect.left > -40:
        #pepe.imagenrect = pepe.imagenrect.move(-1,0)
        pepe.movimiento_x = -1
    if keys[pygame.K_RIGHT] and pepe.imagenrect.right < width + 40:
        #pepe.imagenrect = pepe.imagenrect.move(1,0)
        pepe.movimiento_x = 1 
    
    
    #actualizar movmiento
    pepe.imagenrect = pepe.imagenrect.move(pepe.movimiento_x, pepe.movimiento_y)
    pepe.movimiento_x = 0
    pepe.movimiento_y = 0
    
    
    screen.fill(color)
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_coldown:
        frame += 1
        frame = frame % 2
        last_update = current_time
    screen.blit(pepe.animation_list_idle[frame], pepe.imagenrect)
    pygame.display.flip()
pygame.QUIT