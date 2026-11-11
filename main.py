import pygame
from pygame.mixer_music import play

import constants
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt:float = 0.0
    player:object = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    while True:
        screen.fill("black", rect=None, special_flags=0)
        player.draw(screen)
        pygame.display.flip()
        log_state()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
