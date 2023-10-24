import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center,explosion_anim ):

        super().__init__()
        self.explosion_anim = explosion_anim
        self.explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
        self.image = self.explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # how long to wait for the next frame VELOCITY OF THE EXPLOSION

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                self.kill()  # if we get to the end of the animation we don't keep going.
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center