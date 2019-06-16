#Sons BFXR.NET
#Música PXtone
#Artes feitas com paint.net


import pygame
import random
from os import path
import os

localImg = path.join(path.dirname(__file__), 'img')
localSnd = path.join(path.dirname(__file__), 'snd')



os.environ['SDL_VIDEO_CENTERED'] = '1'


#base
largura = 900
altura = 650
fps = 60


#Cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
amarelo = (225,225,0)
azulnave = (71, 199, 204)
vermelhonave = (204, 71, 93)
vermelhonavevida = (147, 51, 67)
azulnavevida = (63, 177, 181)


#Iniciar
pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
clock = pygame.time.Clock()

nomeFonte = pygame.font.match_font('bitpotion')
def textoDraw(surf, text, size, x, y):
    fonte = pygame.font.Font(nomeFonte, size)
    surfaceTexto = fonte.render(text, True, branco)
    text_rect = surfaceTexto.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(surfaceTexto, text_rect)

def textoDraw2(surf, text, size, x, y):
    fonte = pygame.font.Font(nomeFonte, size)
    surfaceTexto = fonte.render(text, True, branco)
    text_rect = surfaceTexto.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(surfaceTexto, text_rect)

def vidaDraw(surf, x, y, vida, img):
    for i in range(vida):
        imgRect = img.get_rect()
        imgRect.x = x + 30 * i
        imgRect.y = y
        surf.blit(img, imgRect)
        
def vidaDraw2(surf, x, y, vida, img):
    for i in range(vida):
        imgRect = img.get_rect()
        imgRect.x = x + 30 * i
        imgRect.y = y
        surf.blit(img, imgRect)
        
    
#player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerImg, (60, 60))
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, vermelho, self.rect.center, self.radius)
        self.rect.centerx = 200
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0
        self.escudo = 100
        self.delayTiro = 250
        self.ultTiro = pygame.time.get_ticks()
        self.vida = 3
        self.hidden = False
        self.hiddenTempo = pygame.time.get_ticks()

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hiddenTempo> 1000:
            self.hidden = False
            self.rect.center = (200, altura - 10)
            self.escudo = 100
        self.speedx = 0
        self.speedy = 0
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_a]:
            self.speedx = -8
        if tecla[pygame.K_d]:
            self.speedx = 8
        if tecla[pygame.K_s]:
            self.speedy = 8
        if tecla[pygame.K_w]:
            self.speedy = -8
        if tecla[pygame.K_SPACE]:
            self.tiro()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > largura:
                self.rect.right = largura
        if self.rect.left <0:
                self.rect.left = 0
        if self.rect.bottom > altura and self.hidden == False:
                self.rect.bottom = altura
        if self.rect.top < 0:
                self.rect.top = 0

    def tiro(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultTiro > self.delayTiro:
            self.ultTiro = agora
            tiro = Tiros(self.rect.centerx, self.rect.top)
            sprites.add(tiro)
            tiros.add(tiro)
            somTiro.play()

    def hide(self):
        self.hidden = True
        self.hiddenTempo = pygame.time.get_ticks()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura + 1000

#player 2
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerImg2, (60, 60))
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, vermelho, self.rect.center, self.radius)
        self.rect.centerx = 700
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0
        self.escudo = 100
        self.delayTiro = 250
        self.ultTiro = pygame.time.get_ticks()
        self.vida = 3
        self.hidden = False
        self.hiddenTempo = pygame.time.get_ticks()

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hiddenTempo> 1000:
            self.hidden = False
            self.rect.center = (700, altura - 10)
            self.escudo = 100
        
        self.speedx = 0
        self.speedy = 0
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            self.speedx = -8
        if tecla[pygame.K_RIGHT]:
            self.speedx = 8
        if tecla[pygame.K_DOWN]:
            self.speedy = 8
        if tecla[pygame.K_UP]:
            self.speedy = -8
        if tecla[pygame.K_KP_ENTER]:
            self.tiro2()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > largura:
                self.rect.right = largura
        if self.rect.left <0:
                self.rect.left = 0
        if self.rect.bottom > altura and self.hidden == False:
                self.rect.bottom = altura
        if self.rect.top < 0:
                self.rect.top = 0
    def tiro2(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultTiro > self.delayTiro:
            self.ultTiro = agora
            tiro2 = Tiros2(self.rect.centerx, self.rect.top)
            sprites.add(tiro2)
            tiros2.add(tiro2)
            somTiro.play()

    def hide(self):
        self.hidden = True
        self.hiddenTempo = pygame.time.get_ticks()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura +100000

#inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageOrig = random.choice(asteroideImagens)
        self.image = self.imageOrig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 1.85)
        #pygame.draw.circle(self.image, azul, self.rect.center, self.radius)
        self.rect.x = random.randrange(largura - self.rect.width)
        self.rect.y = random.randrange(-250, -200)
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(-2, 2)
        self.rot = 0
        self.velocidadeRot = random.randrange(-8,8)
        self.ultAt = pygame.time.get_ticks()
        
        

    def rotate(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultAt > 50:
            self.ultAt = agora
            self.rot = (self.rot + self.velocidadeRot) % 360
            newImage = pygame.transform.rotate(self.imageOrig, self.rot)
            oldCenter = self.rect.center
            self.image = newImage
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
            
    
    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > altura +10 or self.rect.left < -25 or self.rect.right > largura + 20:
            self.rect.x = random.randrange(largura - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

#asteroide NOVO
def novoasteroide():
    m = Inimigo()
    sprites.add(m)
    inimigos.add(m)
    
#Vida/Escudo
def escudoDraw(surf, x, y, pct):
    if pct < 0:
        pct = 0
    larguraBar = 100
    alturaBar = 10
    fill = (pct / 100) * larguraBar
    borda = pygame.Rect(x , y, larguraBar, alturaBar)
    fillRect = pygame.Rect(x, y, fill, alturaBar)
    pygame.draw.rect(surf, azulnave, fillRect)
    pygame.draw.rect(surf, azulnavevida, borda, 2)

def escudoDraw2(surf, x, y, pct):
    if pct < 0:
        pct = 0
    larguraBar = 100
    alturaBar = 10
    fill = (pct / 100) * larguraBar
    borda = pygame.Rect(x , y, larguraBar, alturaBar)
    fillRect = pygame.Rect(x, y, fill, alturaBar)
    pygame.draw.rect(surf, vermelhonave, fillRect)
    pygame.draw.rect(surf, vermelhonavevida, borda, 2)

#tiros
class Tiros(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laserImg
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self. rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Tiros2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laserImg2
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self. rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

#Explosão
class Explosao(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosaoAnim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.UltUpdate = pygame.time.get_ticks()
        self.frameRate = 50

    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self.UltUpdate > self.frameRate:
            self.UltUpdate = agora
            self.frame += 1
            if self.frame == len(explosaoAnim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosaoAnim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            


#imagens
background = pygame.image.load(path.join(localImg, 'Fundo.png')).convert()
background_rect = background.get_rect()
playerImg = pygame.image.load(path.join(localImg, 'nave.png')).convert_alpha()
playerImgMini = pygame.transform.scale(playerImg, (25, 25))
playerImg2 = pygame.image.load(path.join(localImg, 'nave2.png')).convert_alpha()
player2ImgMini = pygame.transform.scale(playerImg2, (25, 25))
asteroideImagens = []
asteroideLista = ['asteroideGrande1.png', 'asteroideGrande2.png', 'asteroideMedio1.png',
                  'asteroideMedio2.png', 'asteroidePequeno1.png', 'asteroidePequeno2.png',
                  'asteroideMinus.png',]
for img in asteroideLista:
    asteroideImagens.append(pygame.image.load(path.join(localImg, img)).convert_alpha())

laserImg = pygame.image.load(path.join(localImg, 'laser.png')).convert_alpha()
laserImg2 = pygame.image.load(path.join(localImg, 'laser2.png')).convert_alpha()

explosaoAnim = {}
explosaoAnim['grande'] = []
explosaoAnim['pequeno'] = []
explosaoAnim['player'] = []
for i in range(6):
    qualExplosao = 'explosao{}.png'.format(i)
    img = pygame.image.load(path.join(localImg, qualExplosao)).convert_alpha()
    imgGrande = pygame.transform.scale(img, (50, 50))
    explosaoAnim['grande'].append(imgGrande)
    imgPequena = pygame.transform.scale(img, (20, 20))
    explosaoAnim['pequeno'].append(imgPequena)
for img in range(8):
    qualExplosao = 'pexplosao{}.png'.format(img)
    img = pygame.image.load(path.join(localImg, qualExplosao)).convert_alpha()
    imgPlayer = pygame.transform.scale (img, (100, 100))
    explosaoAnim['player'].append(imgPlayer)

#sons e músicas
somTiro = pygame.mixer.Sound(path.join(localSnd, 'Tiro.wav'))
somExplosao = pygame.mixer.Sound(path.join(localSnd, 'Explosão.wav'))
somDano = pygame.mixer.Sound(path.join(localSnd, 'Dano.wav'))
somMorte = pygame.mixer.Sound(path.join(localSnd, 'Morte.wav'))
pygame.mixer.music.load(path.join(localSnd, 'musica1.wav'))
pygame.mixer.music.set_volume(0.8)

            
#Sprites
sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()
tiros2 = pygame.sprite.Group()
player = Player()
player2 = Player2()
sprites.add(player)
sprites.add(player2)
for i in range(15):
   novoasteroide()

score = 0
score2 = 0

pygame.mixer.music.play(loops=-1)
#Jogo
jogando = True
while jogando:
    clock.tick(fps)
    #controles e eventos
    for event in pygame.event.get():
        #sair
        if event.type == pygame.QUIT:
            jogando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if tela == pygame.display.set_mode((largura, altura)):
                    tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
                else:
                    tela = pygame.display.set_mode((largura, altura))                                      
                
                

    #atualização
    sprites.update()

    colisaoBala = pygame.sprite.groupcollide(inimigos, tiros, True, True)
    for colisao in colisaoBala:
        score += 30 - colisao.radius
        somExplosao.play()
        explosão = Explosao(colisao.rect.center, 'grande')
        sprites.add(explosão)
        novoasteroide()

    colisaoBala2 = pygame.sprite.groupcollide(inimigos, tiros2, True, True)
    for colisao in colisaoBala2:
        score2 += 30 - colisao.radius
        somExplosao.play()
        explosão = Explosao(colisao.rect.center, 'grande')
        sprites.add(explosão)
        novoasteroide()

    colisao = pygame.sprite.spritecollide(player, inimigos, True, pygame.sprite.collide_circle)
    for colisoes in colisao:
        player.escudo -= Inimigo().radius * 2
        explosão = Explosao(colisoes.rect.center, 'grande')
        sprites.add(explosão)
        somDano.play()
        novoasteroide()
        if player.escudo <= 0:
            somMorte.play()
            explosaoMorte = Explosao(player.rect.center, 'player')
            sprites.add(explosaoMorte)
            player.hide()
            player.vida -= 1
    if player.vida == 0 and not explosaoMorte.alive():
        jogando = False
        
    colisao2 = pygame.sprite.spritecollide(player2, inimigos, True, pygame.sprite.collide_circle)
    for colisoes in colisao2:
        player2.escudo -= Inimigo().radius * 2
        explosão = Explosao(colisoes.rect.center, 'grande')
        sprites.add(explosão)
        somDano.play()
        novoasteroide()
        if player2.escudo <= 0:
            somMorte.play()
            explosaoMorte = Explosao(player2.rect.center, 'player')
            sprites.add(explosaoMorte)
            player2.hide()
            player2.vida -= 1
    if player2.vida == 0 and not explosaoMorte.alive():
        jogando = False
    
    #renderização
    tela.fill(preto)
    tela.blit(background, background_rect)
    sprites.draw(tela)
    textoDraw(tela, str(score), 40, 150, 1)
    textoDraw2(tela, str(score2), 40, 750, 1)
    escudoDraw(tela, 5, 5, player.escudo)
    escudoDraw2(tela, 795, 5, player2.escudo)
    vidaDraw(tela, largura -890, 30, player.vida, playerImgMini)
    vidaDraw(tela, largura -95, 30, player2.vida, player2ImgMini)
    pygame.display.flip()

pygame.quit()
    
