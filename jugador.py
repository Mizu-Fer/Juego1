import pygame
import imagenes

class player():
    def __init__(self):
        imagen = pygame.image.load("jugador.png").convert_alpha()
        self.imagenespepe = imagenes.spritesheet(imagen)    
    
        self.movimiento_x = 0
        self.movimiento_y = 0
        self.direccion = 0
        self.caminar = False
        
        #animación de imagen
        self.animation_list_idle = []
        self.animation_list_walk = []
        self.animation_steps = 2
        
        self.black = 0, 0, 0
        #agregar imagenes en las listas de animacion
        for x in range(self.animation_steps):
            self.animation_list_idle.append(self.imagenespepe.get_image( x, 0, 48, 48, 3, self.black))
        for x in range(self.animation_steps):
            self.animation_list_walk.append(self.imagenespepe.get_image( x + 2, 0, 48, 48, 3, self.black))
    
        #frame_0 usado como molde xq tienen el mismo tamaño
        self.imagenrect = self.animation_list_idle[0].get_rect()
        self.imagenrect.move_ip(300,100)        
            
    #abajo = 0 , arriba = 1, izquierda = 2, derecha = 3
    def cambiar_direccion(self, una_direccion):
        for x in range(self.animation_steps):
            self.animation_list_idle[x] = self.imagenespepe.get_image( x, una_direccion, 48, 48, 3, self.black)
        for x in range(self.animation_steps):
            self.animation_list_walk[x] = self.imagenespepe.get_image( x + 2, una_direccion, 48, 48, 3, self.black)
        
