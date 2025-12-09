# Design Choices:
### biome rules
-> 

### movement ideas
-> No full regeneration needed.

-> Just redraw the current view each frame

### planned features
-> creatures

-> simulation ticks

-> inventory

-> crafting

-> evolving vegetation

-> weather

-> save/load multiple worlds

-> Python/Pygame rendering layer

-> AI wandering

-> procedural villages

-> erosion

-> species mutation rules

### experiment results
-> 

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