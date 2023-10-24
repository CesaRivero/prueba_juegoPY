import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect()
        self.laser_sound = pygame.mixer.Sound("assets/laser5.ogg")

    def update(self):
        self.rect.y -=4
        if self.rect.bottom < 0:
            self.kill()
