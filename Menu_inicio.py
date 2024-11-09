import pygame

#botones del menu
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    #dibujamos el boton
    def draw(self, surface):
        #variable que devuelve
        action = False
        
        #comprobar click
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False        
            
        #dibujar boton en pantalla
        surface.blit(self.image, self.rect)
        return action