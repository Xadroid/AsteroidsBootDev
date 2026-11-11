import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    _asteroid_field:object = AsteroidField()
    dt:float = 0.0
    _player:object = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    while True:
        screen.fill("black", rect=None, special_flags=0)
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        log_state()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
