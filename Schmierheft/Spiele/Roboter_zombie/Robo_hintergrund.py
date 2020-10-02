import pygame
import sys

pygame.init()              #wichtig um pygame starten zukönnen, initalisierung.

hintergrund = pygame.image.load("Grafiken/hintergrund.png")

screen = pygame.display.set_mode([1200,595]) # groeße des Spielbildschirms.

clock = pygame.time.Clock()           # Zeit muss immer an leigen.

pygame.display.set_caption("Robo gegen Zombie")


def zeichnen():
    screen.blit(hintergrund, (0,0))   
    pygame.draw.rect(screen, (255,0,0), (x,y,breite,hoehe))     
    pygame.display.update()  


x = 300
y = 300
geschw = 3
breite = 40
hoehe = 80


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #anweisung das spiel zu beenden, wenn alles erledigt ist.

    gedrueckt = pygame.key.get_pressed()   # tasten drücken für hoch, runter, links, rechts
    if gedrueckt[pygame.K_UP]:
        y -= geschw
    if gedrueckt[pygame.K_RIGHT]:
        x += geschw    
    if gedrueckt[pygame.K_DOWN]:
        y += geschw
    if gedrueckt[pygame.K_LEFT]:
        x -= geschw   



    zeichnen()

    clock.tick(60) #fps