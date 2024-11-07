import pygame
import imagenes

class player():
    def __init__(self):
        imagen = pygame.image.load("jugador.png").convert_alpha()
        self.imagenespepe = imagenes.spritesheet(imagen)    
    
        self.movimiento_x = 0
        self.movimiento_y = 0
        self.direccion = 0
        self.aceleracion = 5
        self.caminar = False
        
        #animación de imagen
        self.animation_list_idle = []
        self.animation_list_walk = []
        self.animation_steps = 2
        self.animation_coldown = 300
        
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
    
    def movimiento(self, keys, limite_ancho, limite_altura):
        self.caminar = False

        # 40 es la cantidad de pixeles que hay entre el sprite y los bordes de colición
        if keys[pygame.K_UP] and self.imagenrect.top > -40:
            self.movimiento_y = -1
            self.cambiar_direccion(1)
            self.caminar = True

        if keys[pygame.K_DOWN] and self.imagenrect.bottom < limite_altura + 40:
            self.movimiento_y = 1
            self.cambiar_direccion(0)
            self.caminar = True
        
        if keys[pygame.K_RIGHT] and self.imagenrect.right < limite_ancho + 40:
            self.movimiento_x = 1
            self.cambiar_direccion(3)
            self.caminar = True
            
        if keys[pygame.K_LEFT] and self.imagenrect.left > -40:
            self.movimiento_x = -1
            self.cambiar_direccion(2)
            self.caminar = True    
            
        #jugador corre y animación acelera
        if keys[pygame.K_SPACE]:
            self.aceleracion = 2
            self.animation_coldown = 150
        else:
            self.animation_coldown = 300
            self.aceleracion = 5
        
    def actualizar_posicion(self):
        if self.movimiento_x != 0 or self.movimiento_y != 0:
            #actualizar movmiento
            self.imagenrect = self.imagenrect.move(self.movimiento_x, self.movimiento_y)
            self.movimiento_x = 0
            self.movimiento_y = 0
            #delay al movimiento del personaje
            pygame.time.delay(self.aceleracion)
