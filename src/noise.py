from opensimplex import OpenSimplex
import numpy as np

def generate_noise(width, height, seed=0, freq=0.3, octaves=1, lacunarity=2.0, persistence=0.5):
    gen = OpenSimplex(seed)
    def single_noise(x, y):
        return gen.noise2(x, y)
    out = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            nx = x * freq
            ny = y * freq
            amp = 1.0
            freq_i = 1.0
            val = 0.0
            for o in range(octaves):
                val += amp * single_noise(nx * freq_i, ny * freq_i)
                amp *= persistence
                freq_i *= lacunarity
            out[y, x] = val

    # # normalize to 0..255
    # minv, maxv = out.min(), out.max()
    # if maxv - minv == 0:
    #     img = np.zeros_like(out, dtype=np.uint8)
    # else:
    #     img = ((out - minv) / (maxv - minv) * 255.0).astype(np.uint8)
    # return img

    # normalize to 0..1
    minv, maxv = out.min(), out.max()
    if maxv - minv == 0:
        normalized = np.zeros_like(out, dtype=np.float32)
    else:
        normalized = ((out - minv) / (maxv - minv)* 1.0).astype(np.float32)
    return normalized
# 0.0 - 0.25 → deep water  
# 0.25 - 0.35 → coast  
# 0.35 - 0.55 → plains  
# 0.55 - 0.75 → forest  
# 0.75 - 1.0 → mountains
# ~ → water  
# . → plains  
# T → forest  
# ^ → mountains
    
if __name__ == "__main__":
    w, h = 20, 20
    normalized = generate_noise(w, h)
    for row in normalized:
        for v in row:
            if v <=  0.25:
                print("~", end="")
            elif v <= 0.35 and v > 0.25:
                print(".", end="")
            elif v <= 0.55 and v > 0.35:
                print(".", end="")
            elif v <= 0.75 and v > 0.55:
                print("T", end="")
            else:
                print("^", end="")
        print()