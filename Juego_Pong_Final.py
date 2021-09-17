import pygame
import time
negro = 0,0,0
blanco = 255,255,255
light_grey = 200,200,200

def draw_text(surface, text, size, x, y): #Función que mostrará el contador de puntos en pantalla
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, negro)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    pygame.init() #inicia pygame
    size = 800,600 #tamaño de la ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mi primer juego")

    width, height = 800,600
    speed = [2, 2]

    white = 255, 255, 255

    #se carga una imagen
    ball = pygame.image.load('ball.png')
    ballrect = ball.get_rect(center=(width/2,height/2))

    #barra de rebote
    barra = pygame.image.load('barra_final.png')
    barrarect1 = barra.get_rect()
    barrarect2 = barra.get_rect()

    #se ubican las barras en cada lado de la pantalla del jugador
    barrarect1.move_ip(5,230)
    barrarect2.move_ip(779,230)

    clock = pygame.time.Clock()   
    run = True
    #Contador del juego
    marcador_1 = 0
    marcador_2 = 0

    #Definimos las fuentes y declaramos los carteles del Puntaje
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("Puntaje:", 0, (negro)) 
    texto2 = fuente.render("Puntaje:", 0, (negro))

    fuenteSistema = pygame.font.SysFont("Castellar", 50)
    
    while run:
        pygame.time.delay(3) #delay que contralará la velocidad            
        
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False

        #se detecata si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
          if barrarect1.y > 0: 
            barrarect1 = barrarect1.move(0, -3)
        if keys[pygame.K_s]:
          if barrarect1.y < height-barrarect1.height:
            barrarect1 = barrarect1.move(0, 3)

        #Revisa la barra dos 
    
        if keys[pygame.K_UP]:
          if barrarect2.y > 0: 
              barrarect2 = barrarect2.move(0, -3)
       
       
        if keys[pygame.K_DOWN]:
          if barrarect2.y < height-barrarect2.height:
            barrarect2 = barrarect2.move(0, 3)

        #se detemina si hay colisiones 
        if barrarect1.colliderect(ballrect):
            speed[0] = -speed[0]

        if barrarect2.colliderect(ballrect):
            speed[0] = -speed[0]    

        ballrect = ballrect.move(speed) #se mueve el objeto

        #se determinan los límites del objeto
        if ballrect.left <-60 or ballrect.right > width+60:
            if ballrect.left < -60: 
              marcador_2+=1
              
            if ballrect.right > width+60: 
              marcador_1+=1
              

            speed[0] = -speed[0]
            ballrect = ball.get_rect(center=(width/2,height/2))
            time.sleep(1)
            

        if ballrect.top < 0 or ballrect.bottom > height:
          speed[1] = -speed[1]

        #se borra la pantalla anterior con el fondo blanco
        
        screen.fill((3,131,26))
        screen.blit(ball, ballrect)
        screen.blit(barra,barrarect1)
        screen.blit(barra,barrarect2)
        #Linea central
        pygame.draw.aaline(screen, light_grey, (width / 2, 0),(width / 2, height))
        #Circulo central
        pygame.draw.circle(screen, light_grey, ((width / 2),(height / 2)),20)
        
        screen.blit(texto, (0,0))
        screen.blit(texto2, (600,0))
        draw_text(screen, str(marcador_1), 25, 100, 40)
        draw_text(screen, str(marcador_2), 25, 700,40) #Se llama a la función que imprimirá el score en pantalla

        pygame.display.flip()

        
    pygame.quit() #se termina el juego

if __name__ == "__main__":
    main()

