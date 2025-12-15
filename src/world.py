import random
from noise import gen_noise_map, classify, bio_

SPECIES = {
    "rabbit": {
        #color": (180, 255, 180),
        "speed": 4
    },
    "wolf": {
        #"color": (200, 50, 50),
        "speed": 3
    },
    "turtle": {
        #"color": (60, 90, 130),
        "speed": 9
    },
    "sheep": {
        "speed": 6
    }
}

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
        for _ in range(60):
            species_name = random.choice(list(SPECIES.keys()))
            species = SPECIES[species_name]

            creatures.append({
                "x": random.randint(0, self.width - 1),
                "y": random.randint(0, self.height - 1),
                #"color": species["color"],
                "speed": species["speed"],
                "move_tick": 0,
                "species": species_name,
                "behavior": "wander"
            })
        return creatures
