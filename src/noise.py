import os
from opensimplex import OpenSimplex
import numpy as np

# def generate_noise(width, height, seed=0, freq=0.3, octaves=1, lacunarity=2.0, persistence=0.5):
#     gen = OpenSimplex(seed)
#     def single_noise(x, y):
#         return gen.noise2(x, y)
#     out = np.zeros((height, width), dtype=np.float32)
#     for y in range(height):
#         for x in range(width):
#             nx = x * freq
#             ny = y * freq
#             amp = 1.0
#             freq_i = 1.0
#             val = 0.0
#             for o in range(octaves):
#                 val += amp * single_noise(nx * freq_i, ny * freq_i)
#                 amp *= persistence
#                 freq_i *= lacunarity
#             out[y, x] = val
#     minv, maxv = out.min(), out.max()
#     if maxv - minv == 0:
#         normalized = np.zeros_like(out, dtype=np.float32)
#     else:
#         normalized = ((out - minv) / (maxv - minv)* 1.0).astype(np.float32)
#     return normalized
# 0.0 - 0.25 → deep water  
# 0.25 - 0.35 → coast  
# 0.35 - 0.55 → plains  
# 0.55 - 0.75 → forest  
# 0.75 - 1.0 → mountains
# ~ → water  
# . → plains  
# T → forest  
# ^ → mountains
    
# if __name__ == "__main__":
#     w, h = 20, 20
#     normalized = generate_noise(w, h)
#     for row in normalized:
#         for v in row:
#             if v <=  0.25:
#                 print("~", end="")
#             elif v <= 0.35 and v > 0.25:
#                 print(".", end="")
#             elif v <= 0.55 and v > 0.35:
#                 print(".", end="")
#             elif v <= 0.75 and v > 0.55:
#                 print("T", end="")
#             else:
#                 print("^", end="")
#         print()

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

flat = [v for row in grid for v in row]
low = min(flat)
high = max(flat)
normal = []
for row in grid:
    normal.append([(v-low) / (high-low) for v in row])

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
    "symbol": "@"}
view_width = 20
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