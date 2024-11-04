import pygame
import os
pygame.init()
size = 1000, 700

#tamaño d ventana
screen = pygame.display.set_mode(size)

#nombre de ventana
pygame.display.set_caption("juego + épico")


#crear variables

class jugador:
    imagen = pygame.image.load("image.png")
    imagenrect = imagen.get_rect()
    speed = [1, 1]
    def move_forward():
        imagenrect = imagenrect.move(speed)

'''
def movement(imagenrect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        imagenrect=imagenrect.move(0,-1)
    if keys[pygame.K_DOWN]:
        imagenrect=imagenrect.move(0,1)
'''
        
pepe = jugador()
pepe.imagenrect.move_ip(300,100)
#color pantalla
color = 70, 170, 200
#empezar bucle
run = True
while run:
    #ponemos los eventos q ocurren
    for event in pygame.event.get():
        #si es salir de la ventana terminamos
        if event.type == pygame.QUIT: run = False
    
    #movement(pepe.imagenrect)
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP] and pepe.imagenrect.top > 0:
        pepe.imagenrect = pepe.imagenrect.move(0,-1)
    if keys[pygame.K_DOWN] and pepe.imagenrect.bottom < 700:
        pepe.imagenrect = pepe.imagenrect.move(0,1)
    if keys[pygame.K_LEFT] and pepe.imagenrect.left > 0:
        pepe.imagenrect = pepe.imagenrect.move(-1,0)
    if keys[pygame.K_RIGHT] and pepe.imagenrect.right < 1000:
        pepe.imagenrect = pepe.imagenrect.move(1,0) 
    
    #colisión



    screen.fill(color)
    screen.blit(pepe.imagen, pepe.imagenrect)
    pygame.display.flip()
pygame.QUIT