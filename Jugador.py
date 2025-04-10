import pygame
import CONSTANTES

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = pygame.Rect(0,0, CONSTANTES.Ancho_Personaje,CONSTANTES.Alto_Personaje)
        self.forma.center = (x,y)

    def movimiento (self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False    
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def update(self):
        cooldown_animacion = 100   
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index  >= len (self.animaciones):
            self.frame_index = 0
    

        
            
    

    def dibujar(self, interfaz):
      imagen_Flip = pygame.transform.flip (self.image, self.flip, False)
      interfaz.blit (imagen_Flip, self.forma)
      #pygame.draw.rect(interfaz,CONSTANTES.Color_Personaje , self.forma, width=1)






