from opensimplex import OpenSimplex
import numpy as np
from PIL import Image

def generate_noise(width, height, seed=0, freq=0.02, octaves=1, lacunarity=2.0, persistence=0.5):
    gen = OpenSimplex(seed)
    def single_noise(x, y):
        return gen.noise2(x, y)  # returns roughly in [-1,1]

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

    # normalize to 0..255
    minv, maxv = out.min(), out.max()
    if maxv - minv == 0:
        img = np.zeros_like(out, dtype=np.uint8)
    else:
        img = ((out - minv) / (maxv - minv) * 255.0).astype(np.uint8)
    return img

if __name__ == "__main__":
    w, h = 5, 5
    img = generate_noise(w, h, seed=42, freq=0.008, octaves=5, lacunarity=2.0, persistence=0.5)
    print(img)
#    Image.fromarray(img).save("opensimplex_fbm.png")
#    print("Saved opensimplex_fbm.png")
