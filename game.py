import pygame
from player import Player

#creer une class qui represente le jeu
class Game:

    def __init__(self):
        # charger notre joueur
        self.player = Player()
        self.pressed = {}          #dictionnaire = valeur