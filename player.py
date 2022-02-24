import pygame
from projectile import Projectile

#creer une class pour le joueur
class Player(pygame.sprite.Sprite):
    #chargement joueur va appeler init self
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 1

        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/tchoupi1.png')
        #creer ou recuperer un rectangle (deplacement)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity