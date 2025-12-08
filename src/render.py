import pygame
pygame.font.init()
pygame.init()

class Renderer:
    def __init__(self, tile_size, view_width, view_height):
        self.tile_size = tile_size
        self.view_width = view_width
        self.view_height = view_height
        # pygame setup happens here
        width = self.tile_size * self.view_width
        height = self.tile_size * self.view_height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Fractal Wilds")
        font = pygame.font.SysFont("rockwell", 20)

    def draw(self, world, player):
        # draw tiles and player
        self.win.blit(0, 0)