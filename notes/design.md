# Design Choices:
## Implemented
-> creatures

-> AI wandering

-> Python/Pygame rendering layer

## Yet to Implement:
### biome rules
-> Water
##### can't walk on it
##### or: slows movement
##### or: requires a boat later
-> Sand
##### walkable
##### slightly slow? optional
-> Grass
##### normal movement
-> Forest
##### walkable but slower
##### or: reduces visibility later
-> Mountain
##### not walkable
##### or: walkable later with "climbing gear"

### movement ideas
-> No full regeneration needed.

-> Just redraw the current view each frame

### planned features
-> simulation ticks

-> inventory

-> crafting

-> evolving vegetation

-> weather

-> save/load multiple worlds

-> procedural villages

-> erosion

-> species mutation rules

### experiment results
-> 

## Code Layout:
#### world.py → Store and Represent the World
-> saving

-> loading

-> biome queries

-> world rules

-> tile stats

#### noise.py → Terrain Generation & Biome Classification
-> Terrain data

-> OpenSimplex usage

-> noise grid creation

-> normalization

-> classify()

#### main.py → The Game Loop and Viewport Rendering
-> Player Stats

-> Movement code (for now)

#### render.py → The Rendering System File
-> initializing pygame

-> drawing tiles

-> drawing the player

-> refreshing the screen

##### __pycache__ folder is there just for cache to run faster