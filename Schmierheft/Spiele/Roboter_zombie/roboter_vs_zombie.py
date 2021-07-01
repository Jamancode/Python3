#Herzlichen dank an TheDev für die Inspiration zu diesem kleinem Spiel.
#Hier sein Youtube Kanal mit dem Video zum Tutorial.
#Pygame Tutorial https://www.youtube.com/watch?v=6ytwfT3brSc
#___________Bilder und Sounds ____________
#https://github.com/Jamancode/Python3/tree/master/Schmierheft/Spiele/Roboter_zombie
#sounds https://drive.google.com/drive/folders/1zc5Fxq2HLt7BOtXOJaurrSTcZi3A0XhQ
#bilder https://drive.google.com/drive/folders/1NlqB_t_-CHPKFFe_3I9Muslpn-z08iez

#In dem Video von TheDev muss man die Dateinen/Ordner Herunterladen,
#ich habe die Dateinen auch in meinem Github repo zur verfügung gestellt.

import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafiken/hintergrund.png")
screen = pygame.display.set_mode([1200,595])
clock = pygame.time.Clock()
pygame.display.set_caption("HILF ZOMBIE!!!")

angriffLinks = pygame.image.load("Grafiken/angriffLinks.png")
angriffRechts = pygame.image.load("Grafiken/angriffRechts.png")
sprung = pygame.image.load("Grafiken/sprung.png")
rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]
sprungSound = pygame.mixer.Sound("Sounds/sprung.wav")
siegSound = pygame.mixer.Sound("Sounds/robosieg.wav")
verlorenSound = pygame.mixer.Sound("Sounds/robotod.wav")
siegBild = pygame.image.load("Grafiken/sieg.png")
verlorenBild = pygame.image.load("Grafiken/verloren.png")

class spieler:
	def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks):
		self.x = x
		self.y = y
		self.geschw = geschw
		self.breite = breite
		self.hoehe = hoehe
		self.sprungvar = sprungvar
		self.richtg = richtg
		self.schritteRechts = schritteRechts
		self.schritteLinks = schritteLinks
		self.sprung = False
		self.last = [1,0]
		self.ok = True
	def laufen(self,liste):
		if liste[0]:
			self.x -= self.geschw
			self.richtg = [1,0,0,0]
			self.schritteLinks += 1
		if liste[1]:
			self.x += self.geschw
			self.richtg = [0,1,0,0]
			self.schritteRechts += 1
	def resetSchritte(self):
		self.schritteLinks = 0
		self.schritteRechts = 0
	def stehen(self):
		self.richtg = [0,0,1,0]
		self.resetSchritte()
	def sprungSetzen(self):
		if self.sprungvar == -16:
			self.sprung = True
			self.sprungvar = 15
			pygame.mixer.Sound.play(sprungSound)
	def springen(self):
		if self.sprung:
			self.richtg = [0,0,0,1]
			if self.sprungvar >= -15:
				n = 1
				if self.sprungvar < 0:
					n = -1
				self.y -= (self.sprungvar**2)*0.17*n
				self.sprungvar -= 1
			else:
				self.sprung = False
	def spZeichnen(self):
		if self.schritteRechts == 63:
			self.schritteRechts = 0
		if self.schritteLinks == 63:
			self.schritteLinks = 0

		if self.richtg[0]:
			screen.blit(linksGehen[self.schritteLinks//8], (self.x,self.y))
			self.last = [1,0]

		if self.richtg[1]:
			screen.blit(rechtsGehen[self.schritteRechts//8], (self.x,self.y))
			self.last = [0,1]

		if self.richtg[2]:
			if self.last[0]:
				screen.blit(angriffLinks, (self.x,self.y))
			else:
				screen.blit(angriffRechts, (self.x,self.y))

		if self.richtg[3]:
			screen.blit(sprung, (self.x,self.y))

class kugel:
	def __init__(self,spX,spY,richtung,radius,farbe,geschw):
		self.x = spX
		self.y = spY
		if richtung[0]:
			self.x += 5
			self.geschw = -1 * geschw
		elif richtung[1]:
			self.x += 92
			self.geschw = geschw
		self.y += 84
		self.radius = radius
		self.farbe = farbe
	def bewegen(self):
		self.x += self.geschw
	def zeichnen(self):
		pygame.draw.circle(screen, self.farbe, (self.x, self.y), self.radius, 0)

class zombie:
	def __init__(self,x,y,geschw,breite,hoehe,richtg,xMin,xMax):
		self.x = x
		self.y = y
		self.geschw = geschw
		self.breite = breite
		self.hoehe = hoehe
		self.richtg = richtg
		self.schritteRechts = 0
		self.schritteLinks = 0
		self.xMin = xMin
		self.xMax = xMax
		self.leben = 6
		self.linksListe = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
		self.rechtsListe = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
		self.ganz = pygame.image.load("Grafiken/voll.png")
		self.halb = pygame.image.load("Grafiken/halb.png")
		self.leer = pygame.image.load("Grafiken/leer.png")
	def herzen(self):
		if self.leben >= 2:
			screen.blit(self.ganz, (507,15))
		if self.leben >= 4:
			screen.blit(self.ganz, (569,15))
		if self.leben == 6:
			screen.blit(self.ganz, (631,15))

		if self.leben == 1:
			screen.blit(self.halb, (507,15))
		elif self.leben == 3:
			screen.blit(self.halb, (569,15))
		elif self.leben == 5:
			screen.blit(self.halb, (631,15))

		if self.leben <= 0:
			screen.blit(self.leer, (507,15))
		if self.leben <= 2:
			screen.blit(self.leer, (569,15))
		if self.leben <= 4:
			screen.blit(self.leer, (631,15))
	def zZeichnen(self):
		if self.schritteRechts == 63:
			self.schritteRechts = 0
		if self.schritteLinks == 63:
			self.schritteLinks = 0

		if self.richtg[0]:
			screen.blit(self.linksListe[self.schritteLinks//8], (self.x,self.y))
		if self.richtg[1]:
			screen.blit(self.rechtsListe[self.schritteRechts//8], (self.x,self.y))
	def Laufen(self):
		self.x += self.geschw
		if self.geschw > 0:
			self.richtg = [0,1]
			self.schritteRechts += 1
		if self.geschw < 0:
			self.richtg = [1,0]
			self.schritteLinks += 1
	def hinHer(self):
		if self.x > self.xMax:
			self.geschw *= -1
		elif self.x < self.xMin:
			self.geschw *= -1
		self.Laufen()

def zeichnen():
	screen.blit(hintergrund, (0,0))
	for k in kugeln:
		k.zeichnen()
	spieler1.spZeichnen()
	zombie1.zZeichnen()
	zombie1.herzen()
	if gewonnen:
		screen.blit(siegBild,(0,0))
	elif verloren:
		screen.blit(verlorenBild,(0,0))
	pygame.display.update()

def kugelHandler():
	global kugeln
	for k in kugeln:
		if k.x >= 0 and k.x <= 1200:
			k.bewegen()
		else:
			kugeln.remove(k)

def Kollision():
	global kugeln, verloren, gewonnen, go
	zombieRechteck = pygame.Rect(zombie1.x+18,zombie1.y+24,zombie1.breite-36,zombie1.hoehe-24)
	spielerRechteck = pygame.Rect(spieler1.x+18,spieler1.y+36,spieler1.breite-36,spieler1.hoehe-36)

	for k in kugeln:
		kugelRechteck = pygame.Rect(k.x-k.radius,k.y-k.radius,k.radius*2,k.radius*2)
		if zombieRechteck.colliderect(kugelRechteck):
			kugeln.remove(k)
			zombie1.leben -= 1
			if zombie1.leben <= 0 and not verloren:
				gewonnen = True
				pygame.mixer.Sound.play(siegSound)
				go = False

	if zombieRechteck.colliderect(spielerRechteck):
		verloren = True
		gewonnen = False
		pygame.mixer.Sound.play(verlorenSound)
		go = False

linkeWand = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600), 0)
spieler1 = spieler(300,393,4,96,128,-16,[0,0,1,0],0,0)
zombie1 = zombie(600,393,5,96,128,[0,0],40,1090)
verloren = False
gewonnen = False
kugeln = []
go = True
while go:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,96,128)
	gedrueckt = pygame.key.get_pressed()

	if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
		spieler1.laufen([0,1])
	elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
		spieler1.laufen([1,0])
	else:
		spieler1.stehen()

	if gedrueckt[pygame.K_UP]:
		spieler1.sprungSetzen()
	spieler1.springen()

	if gedrueckt[pygame.K_SPACE]:
		if len(kugeln) <= 0 and spieler1.ok:
			kugeln.append(kugel(round(spieler1.x),round(spieler1.y),spieler1.last,8,(0,0,0),7))
		spieler1.ok = False

	if not gedrueckt[pygame.K_SPACE]:
		spieler1.ok = True

	kugelHandler()
	zombie1.hinHer()

	Kollision()
	zeichnen()
	clock.tick(60)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	zeichnen()