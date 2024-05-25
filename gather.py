# pyright: reportArgumentType=false

from build_maze import plant_maze
from crops import carrots, grass, pumpkins, wood
from move_util import goto
from set_ground import clear_unwanted
from solve_maze import left_wall_solve

HAY = 5000
WOOD = 5000
CARROT = 5000
PUMPKIN = 5000
GOLD = 5000

goto(0)
while True:
    while num_items(Items.Gold) < GOLD:
        if num_items(Items.Pumpkin) < 500:
            # need pumpkins for fertilizer
            break

        plant_maze()
        left_wall_solve()

    if num_items(Items.Pumpkin) < PUMPKIN:
        clear_unwanted(Entities.Pumpkin, Grounds.Soil)
    while num_items(Items.Pumpkin) < PUMPKIN:
        if num_items(Items.Carrot) < 10:
            break
        pumpkins()

    if num_items(Items.Carrot) < CARROT:
        clear_unwanted(Entities.Carrots, Grounds.Soil)
    while num_items(Items.Carrot) < CARROT:
        if num_items(Items.Hay) < 10 or num_items(Items.Wood) < 10:
            break
        carrots()

    if num_items(Items.Hay) < HAY:
        clear_unwanted(Entities.Grass, Grounds.Turf)
    while num_items(Items.Hay) < HAY:
        grass()

    if num_items(Items.Wood) < WOOD:
        clear_unwanted(Entities.Bush, Grounds.Turf)
    while num_items(Items.Wood) < WOOD:
        wood()
