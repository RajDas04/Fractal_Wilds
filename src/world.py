from noise import gen_noise_map, classify, bio_

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.generate()

    def generate(self):
        terrain = []
        for row in gen_noise_map(self.width, self.height):
            terrain.append([classify(v) for v in row])
        return terrain
    
    def get_symbol(self,x,y):
        biome = self.map[y][x] 
        return bio_[biome]["symbol"]