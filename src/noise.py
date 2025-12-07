from opensimplex import OpenSimplex

def gen_noise_map(width, height, scale = 20, seed = 42):
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
    return normal

# Creating the map
def classify(value):
    if value < 0.25: return "water"
    if value < 0.45: return "sand"
    if value < 0.65: return "grass"
    if value < 0.85: return "forest"
    return "mountain"

bio_ = {
    "water":    {"symbol": "~", "color": "#00d7d7"},
    "sand":     {"symbol": ".", "color": "#e1e100"},
    "grass":    {"symbol": "T", "color": "#00ca00"},
    "forest":   {"symbol": "^", "color": "#006c00"},
    "mountain": {"symbol": "M", "color": "#c0c0c0"}}