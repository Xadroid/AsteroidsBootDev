import pygame

import constants
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
