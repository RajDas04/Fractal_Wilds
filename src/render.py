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
        self.tile_images = {
            "water": pygame.image.load("data/assets/water_pixel.png").convert_alpha(),
            "sand": pygame.image.load("data/assets/sand_pixel.png").convert_alpha(),
            "grass": pygame.image.load("data/assets/grass_pixel.png").convert_alpha(),
            "forest": pygame.image.load("data/assets/forest_pixel.png").convert_alpha(),
            "mountain": pygame.image.load("data/assets/mountain_pixel.png").convert_alpha(),
        }
        self.player_image = pygame.transform.scale(
            pygame.image.load("data/assets/player_pixel.png").convert_alpha(), (self.tile_size, self.tile_size))
        for key in self.tile_images:
            self.tile_images[key]  = pygame.transform.scale(self.tile_images[key], (self.tile_size, self.tile_size))

    def draw(self, world, player):
        self.win.fill((0,0,0))
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
                screen_x = col * self.tile_size
                screen_y = row * self.tile_size
                self.win.blit(self.tile_images[biome], (screen_x, screen_y))

        for c in world.creatures:
            sx = (c["x"] - cam_left) * self.tile_size
            sy = (c["y"] - cam_top) * self.tile_size
            pygame.draw.circle(self.win, c["color"], (sx + 12, sy + 12), 6)

        player_screen_x = (player["x"] - cam_left) * self.tile_size
        player_screen_y = (player["y"] - cam_top) * self.tile_size
        self.win.blit(self.player_image, (player_screen_x, player_screen_y))

        pygame.display.flip()