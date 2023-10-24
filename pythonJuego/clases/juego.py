import random

import pygame

from clases import conexion
from clases.conexion import Conexion
from clases.explosiones import Explosion
from clases.variables import ancho, color_negro, alto, color_azul, color_rojo
from clases.jugador import Jugador
from clases.laser import Laser
from clases.meteoro import Meteoro
from clases.variables import ancho


class Juego(object):
    def __init__(self,):
        self.player_name=None
        self.laser = Laser()
        self.game_over = False
        self.score =0
        self.lista_meteoros = pygame.sprite.Group()
        self.lista_sprite = pygame.sprite.Group()
        self.lista_laser = pygame.sprite.Group()
        self.cantidad_meteoro=10

        for i in range(self.cantidad_meteoro):
            meteoro = Meteoro()
            meteoro.rect.x = random.randrange(ancho - 20)
            meteoro.rect.y = random.randrange(450)
            self.lista_meteoros.add(meteoro)
            self.lista_sprite.add(meteoro)

        self.jugador = Jugador()
        self.lista_sprite.add(self.jugador)
        self.explosion_anim = []

        for i in range(9):
            file = "assets/regularExplosion0{}.png".format(i)
            img = pygame.image.load(file).convert()
            img.set_colorkey( color_negro)
            img_scale = pygame.transform.scale(img, (70, 70))
            self.explosion_anim.append(img_scale)

    def set_player_name(self, name):
        self.player_name = name

    def eventos(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            if evento.type==pygame.MOUSEBUTTONDOWN:
                laser= Laser()
                laser.rect.x = self.jugador.rect.x +45
                laser.rect.y = self.jugador.rect.y -20
                laser.laser_sound.play()
                self.lista_sprite.add(laser)
                self.lista_laser.add(laser)
                if self.game_over:
                    self.__init__()
        return False

    def logica(self):
        if not self.game_over:
            self.lista_sprite.update()
        hits = pygame.sprite.spritecollide(self.jugador,self.lista_meteoros,True)
        for hit in hits:
            self.jugador.vida-=1
            if self.jugador.vida<1:
                self.game_over = True



        #colision meteoro-laser
        hits=pygame.sprite.groupcollide(self.lista_meteoros,self.lista_laser,True,True)

        for hit in hits:
            explosion = Explosion(hit.rect.center, self.explosion_anim)
            explosion.explosion_sound.play()
            self.lista_sprite.add(explosion)
            meteoro = Meteoro()
            self.lista_meteoros.add(meteoro)
            self.lista_sprite.add(meteoro)
            self.score += 1

    def draw_text(surface,text,size,x,y):#buscar como sustituir abajo,no agarra todos los argumentos
        font = pygame.font.SysFont("comic sans", size)
        text_surface = font.render(text, True, color_azul)
        text_rect= text_surface.get_rect()
        text_rect.midtop=(x,y)
        surface.blit(text_surface,text_rect)

    def vista_ventana(self,ventana):
        ventana.fill(color_negro)
        background = pygame.image.load("background.png").convert()
        if self.game_over:
            font = pygame.font.SysFont("comic sans",30)
            text = font.render("Fin del Juego, haz clic para continuar",True,color_rojo)
            center_x=(ancho//2) - (text.get_width()//2)
            center_y= (alto//2)- (text.get_height()//2)
            ventana.blit(text,[center_x,center_y])
            

        if not self.game_over:
            ventana.blit(background, [0, 0])
            self.lista_sprite.draw(ventana)

            font = pygame.font.SysFont("comic sans", 30)
            vida_texto = "VIDA: " + str(self.jugador.vida)
            text = font.render(vida_texto, True, color_azul)
            center_x = (ancho // 2) - (text.get_width() // 2)
            center_y = (15) - (text.get_height() // 2)
            ventana.blit(text, [center_x, center_y])

            score_texto = "Score: " + str(self.score)
            text = font.render(score_texto, True, color_rojo)
            center_x = (15 )
            center_y = (15 )
            ventana.blit(text, [center_x, center_y])
        pygame.display.flip()

    def mostrar_pantalla_inicio(self, ventana):
        player_name = ""
        input_active = True
        font = pygame.font.SysFont("comic sans", 30)
        color_inactive = (255, 255, 255)
        color_active = (255, 0, 0)
        color = color_active

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

            ventana.fill((0, 0, 0))
            text = font.render(f"Ingresa tu nombre: {player_name}", True, color)
            text_rect = text.get_rect(center=(ancho // 2, alto // 2))
            ventana.blit(text, text_rect)
            pygame.display.flip()

        return player_name
