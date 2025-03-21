import pygame
import sys
from src.settings import WIDTH, HEIGHT, MARGIN_BOTTOM
from src.game import Game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + MARGIN_BOTTOM))
pygame.display.set_caption('Pacman')


class Main:
    def __init__(self, screen, background_color, walls_color):
        self.screen = screen
        self.FPS = pygame.time.Clock()
        self.initial_background_color = background_color
        self.initial_walls_color = walls_color

    def start(self):
        game = Game(self.screen)
        
        if self.initial_background_color:
            while game.background_color != self.initial_background_color:
                game.change_background_color()
        if self.initial_walls_color:
            while game.walls_color != self.initial_walls_color:
                game.change_walls_color()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game.is_pause = not game.is_pause
                    if event.key == pygame.K_m:
                        game.is_pause = False
                        game.is_menu_open = True
                        
            if not game.is_pause:
                game.draw() 
            else:
                game.display.show_pause(self.screen)

            pygame.display.update()
            self.FPS.tick(30)

if __name__ == '__main__':

    play = Main(screen)
    play.start()