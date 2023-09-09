import pygame, sys
from settings import *
from debug import debug
from level import *

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        pygame.display.set_caption('The Legend of Zelda')
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('dark green')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()