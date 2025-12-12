from render import Renderer
from world import World
import os
import pygame

world = World(500,500)
player = {"x":25,"y":25,"symbol":"()"}
view_width = 30
view_height = 12

TILE_SIZE = 35
VIEW_WIDTH = 35
VIEW_HEIGHT = 18

USE_PYGAME = True  # change to True to use pygame and False to use terminal ASCII

if USE_PYGAME == False: # ASCII map
    def cam_render():
        camera_left = player["x"] - view_width //2
        camera_right  = camera_left + view_width
        camera_top    = player["y"] - view_height // 2
        camera_bottom = camera_top + view_height

        print("\n Camera View:")
        for y in range(camera_top, camera_bottom):
            row_str = ""
            for x in range(camera_left, camera_right):
                if x < 0 or x >= world.width or y < 0 or y >= world.height:
                    row_str += " "
                    continue
                if x == player["x"] and y == player["y"]:
                    row_str += player["symbol"]
                else:
                    row_str += world.get_symbol(x, y)
            print(row_str)

        cam_render()
        while True:
            command = input("To move, press WASD and Q to quit: ").lower()
            if command == "w" and player["y"] > 0:
                player["y"] -= 1
            elif command == "s" and player["y"] < world.height -1:
                player["y"] +=1
            elif command == "a" and player["x"] > 0:
                player["x"] -=1
            elif command == "d" and player["x"] < world.width -1:
                player["x"] +=1
            elif command == "q":
                break
            else:
                print("Invalid Command...")
                continue
            os.system("cls" if os.name == "nt" else "clear")
            cam_render()

if USE_PYGAME == True: # Pygame 
    def try_move(dx, dy):
        new_x = player["x"] + dx
        new_y = player["y"] + dy

        if 0 <= new_x < world.width and 0 <= new_y < world.height:
            biome = world.map[new_y][new_x]
        if biome not in ("water", "mountain"):
            player["x"] = new_x
            player["y"] = new_y

    renderer = Renderer(TILE_SIZE, VIEW_WIDTH, VIEW_HEIGHT)  
    clock = pygame.time.Clock()
    current_time = pygame.time.get_ticks()
    move_cooldown = 100 # ms
    last_move_time = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(30)
        keys = pygame.key.get_pressed()
        new_x = player["x"]
        new_y = player["y"]
        current_time = pygame.time.get_ticks()

        if current_time - last_move_time > move_cooldown:
            if keys[pygame.K_w] and player["y"] > 0:
                try_move(0, -1)
                last_move_time = current_time
            if keys[pygame.K_s] and player["y"] < world.height -1:
                try_move(0, +1)
                last_move_time = current_time
            if keys[pygame.K_a] and player["x"] > 0:
                try_move(-1, 0)
                last_move_time = current_time
            if keys[pygame.K_d] and player["x"] < world.width -1:
                try_move(+1, 0)
                last_move_time = current_time

        renderer.draw(world, player)