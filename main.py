import pygame
pygame.init()
from game import Game

# Fenetre
pygame.display.set_caption("Zozo Game")
screen = pygame.display.set_mode((1080, 720))

#importation de l'arriere plan
background = pygame.image.load('assets/bg.jpg')

#charger notre jeu
game = Game()

running = True

while running:
    #appliquer l'arriere plan
    screen.blit(background, (0, -200))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    #recup les projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    #appliquer l'ensemblke des images des projectiles
    game.player.all_projectiles.draw(screen)

    #verifier si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 1:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < screen.get_width():
        game.player.move_down()


    #maj de l'ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier que l'event est la fermeture dfe la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si le joueur utilise le clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est touchee
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

