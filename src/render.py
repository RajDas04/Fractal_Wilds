import pygame

class Renderer:
    def __init__(self, tile_size, view_width, view_height):
        self.tile_size = tile_size
        self.view_width = view_width
        self.view_height = view_height
        pygame.init()
        pygame.font.init()
        self.width = self.tile_size * self.view_width
        self.height = self.tile_size * self.view_height
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fractal Wilds")
        self.font = pygame.font.SysFont("rockwell", 20)

    def draw(self, world, player):
        self.win.fill((0, 0, 0))
        cam_left = player["x"] - self.view_width //2
        cam_right  = cam_left + self.view_width
        cam_top    = player["y"] - self.view_height // 2
        cam_bottom = cam_top + self.view_height

        for row in range(self.view_height):
            for col in range(self.view_width):
                world_x = cam_left + col
                world_y = cam_top + row
                pass
        pygame.display.flip()