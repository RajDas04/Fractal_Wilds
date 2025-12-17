import random
from noise import gen_noise_map, classify, bio_

SPECIES = {
    "rabbit": {
        "speed": 4,
        "allowed_biome": {"forest", "grass"}
    },
    "wolf": {
        "speed": 3,
        "allowed_biome": {"forest", "grass", "mountain", "sand"}
    },
    "turtle": {
        "speed": 9,
        "allowed_biome": {"sand", "water"}
    },
    "sheep": {
        "speed": 6,
        "allowed_biome": {"forest", "grass"}
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
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.map[y][x] in species["allowed_biome"]:
                    creatures.append({
                        "x": x,
                        "y": y,
                        "speed": species["speed"],
                        "move_tick": 0,
                        "species": species_name,
                        "behavior": "wander",
                        "allowed_biome": species["allowed_biome"],
                        "anim_state": "idle",
                        "anim_frame": 0
                    })
                    break
        return creatures
