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

        self.animation_tick = 0
        self.animation_speed = 6
        self.animation_frame = 0

        self.tile_images = {
            "water":[
                pygame.image.load("data/assets/water_pixel_0.png").convert_alpha(),
                pygame.image.load("data/assets/water_pixel_1.png").convert_alpha(),
                pygame.image.load("data/assets/water_pixel_2.png").convert_alpha(),
                pygame.image.load("data/assets/water_pixel_3.png").convert_alpha()
            ],
            "sand": [pygame.image.load("data/assets/sand_pixel.png").convert_alpha()],
            "grass":[
                pygame.image.load("data/assets/grass_pixel_0.png").convert_alpha(),
                pygame.image.load("data/assets/grass_pixel_1.png").convert_alpha(),
                pygame.image.load("data/assets/grass_pixel_2.png").convert_alpha()
            ],
            "forest": [pygame.image.load("data/assets/forest_pixel.png").convert_alpha()],
            "mountain": [pygame.image.load("data/assets/mountain_pixel.png").convert_alpha()],
        }
        for biome, frames in self.tile_images.items():
            self.tile_images[biome] = [pygame.transform.scale(frame, (self.tile_size, self.tile_size))
                                       for frame in frames]

        self.player_image = pygame.transform.scale(
            pygame.image.load("data/assets/player_pixel_idle.png").convert_alpha(), (self.tile_size, self.tile_size))

        self.creature_images = {
            "rabbit": {
                "idle":[
                    pygame.transform.scale(pygame.image.load("data/assets/rabbit_pixel_idle.png").convert_alpha(),
                    (self.tile_size, self.tile_size))
                ],
                "walk":[
                    pygame.transform.scale(pygame.image.load("data/assets/rabbit_pixel_walk1.png").convert_alpha(),
                        (self.tile_size, self.tile_size)),
                    pygame.transform.scale(pygame.image.load("data/assets/rabbit_pixel_walk2.png").convert_alpha(),
                        (self.tile_size, self.tile_size))
                ]
            },
            "wolf": {
                "idle":[
                    pygame.transform.scale( pygame.image.load("data/assets/wolf_pixel_idle.png").convert_alpha(),
                    (self.tile_size, self.tile_size))
                ],
                "walk":[
                    pygame.transform.scale(pygame.image.load("data/assets/wolf_pixel_walk1.png").convert_alpha(),
                        (self.tile_size, self.tile_size)),
                    pygame.transform.scale(pygame.image.load("data/assets/wolf_pixel_walk2.png").convert_alpha(),
                        (self.tile_size, self.tile_size))
                ]
            },
            "turtle": pygame.transform.scale(pygame.image.load("data/assets/turtle_pixel_idle.png").convert_alpha(),
                (self.tile_size, self.tile_size)),
            "sheep": {
                "idle":[
                    pygame.transform.scale(pygame.image.load("data/assets/sheep_pixel_idle.png").convert_alpha(),
                (self.tile_size, self.tile_size))],
                "walk":[
                    pygame.transform.scale(pygame.image.load("data/assets/sheep_pixel_walk1.png").convert_alpha(),
                        (self.tile_size, self.tile_size)),
                    pygame.transform.scale(pygame.image.load("data/assets/sheep_pixel_walk2.png").convert_alpha(),
                        (self.tile_size, self.tile_size))
                ]
            }
        }

    def draw(self, world, player):
        self.win.fill((0,0,0))
        cam_left = player["x"] - self.view_width //2
        cam_top = player["y"] - self.view_height // 2
        
        while True: # tile section
            self.animation_tick += 1
            if self.animation_tick >= self.animation_speed:
                self.animation_tick = 0
                self.animation_frame += 1
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
                    frames = self.tile_images[biome]
                    frame_gen = frames[self.animation_frame % len(frames)]
                    self.win.blit(frame_gen, (screen_x, screen_y))
            break

        while True: # creature section
            for c in world.creatures:
                sx = (c["x"] - cam_left) * self.tile_size
                sy = (c["y"] - cam_top) * self.tile_size
                d = self.creature_images[c["species"]]
                if isinstance(d, dict):
                    frames = d[c["anim_state"]]
                    self.win.blit(frames[c["anim_frame"]], (sx, sy))
                    c["anim_tick"] += 1
                    if c["anim_tick"] >= c["anim_delay"]:
                        c["anim_tick"] = 0
                        c["anim_frame"] = (c["anim_frame"] + 1) % len(frames)
                else:
                    self.win.blit(d, (sx, sy))
            break

        player_screen_x = (player["x"] - cam_left) * self.tile_size
        player_screen_y = (player["y"] - cam_top) * self.tile_size
        self.win.blit(self.player_image, (player_screen_x, player_screen_y))

        pygame.display.flip()