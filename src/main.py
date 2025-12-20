from render import Renderer
from world import World
import os
import pygame
import random

world = World(250,250)
player = {"x":25,"y":25,"symbol":"()"}
view_width = 30 # used for ASCII
view_height = 12 # used for ASCII

TILE_SIZE = 30 # used for Pygame
VIEW_WIDTH = 35 # used for Pygame
VIEW_HEIGHT = 18 # used for Pygame

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
    def reset_animation(creature, new):
        if creature["anim_state"] != new:
            creature["anim_state"] = new
            creature["anim_frame"] = 0

    def wander(creature):
        dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)]) # pick random direction
        new_x = creature["x"] + dx
        new_y = creature["y"] + dy
        if not (0 <= new_x < world.width and 0 <= new_y < world.height):
            reset_animation(creature, "idle")
            return False
        biome = world.map[new_y][new_x]
        if biome not in creature["allowed_biome"]:
            reset_animation(creature, "idle")
            return False
        creature["x"] = new_x
        creature["y"] = new_y
        reset_animation(creature, "walk")
        return True

    renderer = Renderer(TILE_SIZE, VIEW_WIDTH, VIEW_HEIGHT)  
    clock = pygame.time.Clock()
    creatures = world.creatures
    run = True
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        new_x = player["x"]
        new_y = player["y"]

        for c in creatures:
            c["move_tick"] += 1
            if c["move_tick"] >= c["speed"]:
                wander(c)
                c["move_tick"] = 0

        if keys[pygame.K_w] and player["y"] > 0:
            new_y -= 1
        if keys[pygame.K_s] and player["y"] < world.height - 1:
            new_y += 1
        if keys[pygame.K_a] and player["x"] > 0:
            new_x -= 1
        if keys[pygame.K_d] and player["x"] < world.width - 1:
            new_x += 1
        if keys[pygame.K_q]:
            break
        if 0 <= new_x < world.width and 0 <= new_y < world.height:
            biome = world.map[new_y][new_x]
            if biome not in ("water", "mountain"):
                player["x"] = new_x
                player["y"] = new_y

        renderer.draw(world, player)