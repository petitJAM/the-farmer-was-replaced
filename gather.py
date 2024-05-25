# pyright: reportArgumentType=false

from build_maze import plant_maze
from crops import carrots, grass, pumpkins, wood
from return_home import return_home
from solve_maze import left_wall_solve

HAY = 5000
WOOD = 5000
CARROT = 5000
PUMPKIN = 5000
GOLD = 5000

return_home()
while True:
    while num_items(Items.Gold) < GOLD:
        if num_items(Items.Pumpkin) < 500:
            # need pumpkins for fertilizer
            break

        plant_maze()
        left_wall_solve()


    while num_items(Items.Pumpkin) < PUMPKIN:
        if num_items(Items.Carrot) < 10:
            break
        pumpkins()
        
    while num_items(Items.Carrot) < CARROT:
        if num_items(Items.Hay) < 10 or num_items(Items.Wood) < 10:
            break
        carrots()
        
    while num_items(Items.Hay) < HAY:
        grass()
        
    while num_items(Items.Wood) < WOOD:
        wood()
