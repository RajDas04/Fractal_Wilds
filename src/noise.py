import os
from opensimplex import OpenSimplex

width = 50
height = 50
scale = 20
seed = 42

noise = OpenSimplex(seed)
grid = []
for y in range(height):
    row = []
    for x in range(width):
        value = noise.noise2(x/scale, y/scale)
        row.append(value)
    grid.append(row)

# normalize the values within 0 to 1 will be floats
flat = [v for row in grid for v in row]
low = min(flat)
high = max(flat)
normal = []
for row in grid:
    normal.append([(v-low) / (high-low) for v in row])

# Creating the map
def classify(value):
    if value < 0.25: return "water"
    if value < 0.45: return "sand"
    if value < 0.65: return "grass"
    if value < 0.85: return "forest"
    return "mountain"
    
terrain = []
for row in normal:
    terrain.append([classify(v) for v in row])
symbols = {
    "water": "~",
    "sand": ".",
    "grass": "T",
    "forest": "^",
    "mountain": "M"}
ascii_map = []
for row in terrain:
    ascii_map.append("".join(symbols[cell] for cell in row))
# for line in ascii_map:
#     print(line)

# Camera view of the map with player movement
player = {
    "x": width // 2,
    "y": height // 2,
    "symbol": "()"}
view_width = 30
view_height = 12

def cam_movement():
    camera_left = player["x"] - view_width //2
    camera_right  = camera_left + view_width
    camera_top    = player["y"] - view_height // 2
    camera_bottom = camera_top + view_height

    print("\n Camera View:")
    for ty in range(camera_top, camera_bottom):
        row_str = ""
        for tx in range(camera_left, camera_right):
            if tx < 0 or tx >= width or ty < 0 or ty >= height:
                row_str += " "
                continue
            if tx == player["x"] and ty == player["y"]:
                row_str += player["symbol"]
            else:
                row_str += symbols[terrain[ty][tx]]
        print(row_str)

cam_movement()
while True:
    command = input("To move, press WASD and Q to quit: ").lower()
    if command == "w" and player["y"] > 0:
        player["y"] -= 1
    elif command == "s" and player["y"] < height -1:
        player["y"] +=1
    elif command == "a" and player["x"] > 0:
        player["x"] -=1
    elif command == "d" and player["x"] < width -1:
        player["x"] +=1
    elif command == "q":
        break
    else:
        print("Not a valid command.")
        continue
    os.system("cls" if os.name == "nt" else "clear")
    cam_movement()