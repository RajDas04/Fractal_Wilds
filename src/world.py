import random
from noise import gen_noise_map, classify, bio_

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.generate()
        self.creatures = self.live_creature()

    def generate(self):
        terrain = []
        for row in gen_noise_map(self.width, self.height):
            terrain.append([classify(v) for v in row])
        return terrain
    
    def get_symbol(self,x,y):
        biome = self.map[y][x] 
        return bio_[biome]["symbol"]
    
    def live_creature(self):
        creatures = []
        for _ in range(20):
            creatures.append({
                "x": random.randint(0, self.width-1),
                "y": random.randint(0, self.height-1),
                "color": (255, 0, 0),
                "symbol": "c",
                "behavior": "wander"
            })
        return creatures
