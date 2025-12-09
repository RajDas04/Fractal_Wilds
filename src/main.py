from render import Renderer
from world import World
import os

world = World(50,50)
player = {"x":25,"y":25,"symbol":"()","color":"#ff0000"}
view_width = 30
view_height = 12
RENDER_MODE = "pygame"

TILE_SIZE = 24
VIEW_WIDTH = 30
VIEW_HEIGHT = 15

USE_PYGAME = False  # change to True when ready

Renderer.draw(world, player)

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