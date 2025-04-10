import pygame
import pytmx
import sys
import CONSTANTES 
from Jugador import Personaje
pygame.init()


ventana = pygame.display.set_mode((CONSTANTES.Ancho_Ventana, CONSTANTES.Alto_Ventana))
pygame.display.set_caption('Drug hunt')

#Defino Variables del movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False
saltar = False
#Controlar fps 

reloj = pygame.time.Clock()

fondo_original = pygame.image.load("C:/Users/sergi/Desktop/PPI JUEGO DEFINITIVO/PRIMER-JUEGO/assets/recursos/fondo/Background.png").convert()

fondo = pygame.transform.scale(fondo_original,(CONSTANTES.Ancho_Ventana,CONSTANTES.Alto_Ventana))

#ventana.blit (fondo,(0,0))
#ventana.fill(CONSTANTES.Color_Fondo)
#lista de animaciones
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size= (w*scale,h*scale))
    return nueva_imagen
animaciones = []
for i in range (6):
    img = pygame.image.load(f"C:/Users/sergi/Desktop/PPI JUEGO DEFINITIVO/PRIMER-JUEGO/assets/recursos/personaje/soldado/run{i}.png").convert_alpha()
    img = escalar_img (img, CONSTANTES.Scala_personaje)
    animaciones.append(img)
#importar imagen al jugador
jugador = Personaje (x= 50, y= 550,animaciones=animaciones)
#importar mapa
from pytmx import load_pygame
tmx_data = load_pygame("C:/Users/sergi/Desktop/PPI JUEGO DEFINITIVO/PRIMER-JUEGO/assets/recursos/mapa/mapa.tmx")
#colisiones del mapa

def render_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer:
                tile_image = tmx_data.get_tile_image_by_gid(tile)
                if tile_image:
                    ventana.blit(tile_image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    
   
while True:
    #delay
    
    pygame.time.delay(0)

  

    
    #Valor fps

    reloj.tick(CONSTANTES.fps)
    ventana.fill(CONSTANTES.Color_Fondo)
    ventana.blit (fondo,(0,0))
    



    #calcular movimiento del jugador

    delta_x = 0
    delta_y = 0

    
    if mover_derecha == True:
        delta_x =   CONSTANTES.velocidad

    if mover_izquierda == True:
        delta_x = -CONSTANTES.velocidad

    if mover_abajo == True:
        delta_y = CONSTANTES.velocidad

    if mover_arriba == True:
        delta_y = -CONSTANTES.velocidad

    #mover jugador
    
    jugador.movimiento(delta_x, delta_y) 

    jugador.update()
        
    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True   
            if event.key == pygame.K_d:
                mover_derecha = True  
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

     #Para cuando se suelte la tecla

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False   
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

       #evento para saltar
        
         # Renderizar el mapa
    render_map()         



    pygame.display.update()            
