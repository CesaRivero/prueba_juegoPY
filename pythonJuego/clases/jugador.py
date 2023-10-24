import pygame

from clases.variables import color_negro, ancho, alto


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vida = 5
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(color_negro)
        self.rect = self.image.get_rect()
        self.rect.centerx=ancho//2
        self.rect.centery=alto -50
        self.speed_x=0
        self.speed_y=0

    def update(self):
        self.speed_x=0
        self.speed_y =0
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed_x = -5
        if keystate[pygame.K_d]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        if keystate[pygame.K_w]:
            self.speed_y = -5
        if keystate[pygame.K_s]:
            self.speed_y = 5
        self.rect.y += self.speed_y

        if self.rect.right>ancho:
            self.rect.right=ancho
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > alto:
            self.rect.bottom = alto
