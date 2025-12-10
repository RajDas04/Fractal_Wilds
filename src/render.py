import pygame
from noise import bio_, player_

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
        #self.win.fill((0, 0, 0))
        cam_left = player["x"] - self.view_width //2
        cam_top = player["y"] - self.view_height // 2

        for row in range(self.view_height):
            for col in range(self.view_width):
                world_x = cam_left + col
                world_y = cam_top + row
                
                if (world_x < 0 or world_x >= world.width or
                    world_y < 0 or world_y >= world.height):
                    continue

                biome = world.map[world_y][world_x]
                color = bio_[biome]["color"]
                screen_x = col * self.tile_size
                screen_y = row * self.tile_size
                pygame.draw.rect(self.win, color, (screen_x, screen_y, self.tile_size, self.tile_size))

                player_screen_x = (player["x"] - cam_left) * self.tile_size
                player_screen_y = (player["y"] - cam_top) * self.tile_size
                pygame.draw.rect(self.win,player_,
                                 (player_screen_x, player_screen_y, self.tile_size, self.tile_size))

        #pygame.display.flip()
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()