# pyright: reportArgumentType=false

from build_maze import plant_maze
from crops import carrots, grass, pumpkins, wood
from move_util import goto
from set_ground import clear_unwanted
from solve_maze import left_wall_solve
from sunflowers import sunflowers

reqs = {
    Items.Hay: 1000,
    Items.Wood: 1000,
    Items.Carrot: 1000,
    Items.Pumpkin: 1000,
    Items.Gold: 1000,
    Items.Power: 1000,
}

goto(0)
while True:
    quick_print(reqs)

    if num_items(Items.Hay) < reqs[Items.Hay]:
        clear_unwanted(Entities.Grass, Grounds.Turf)
        while num_items(Items.Hay) < reqs[Items.Hay]:
            grass()
    else:
        reqs[Items.Hay] += 1000

    if num_items(Items.Wood) < reqs[Items.Wood]:
        clear_unwanted(Entities.Bush, Grounds.Turf)
        while num_items(Items.Wood) < reqs[Items.Wood]:
            wood()
    else:
        reqs[Items.Wood] += 1000

    if num_items(Items.Carrot) < reqs[Items.Carrot]:
        clear_unwanted(Entities.Carrots, Grounds.Soil)
        while num_items(Items.Carrot) < reqs[Items.Carrot]:
            if num_items(Items.Hay) < 10 or num_items(Items.Wood) < 10:
                break
            carrots()
    else:
        reqs[Items.Carrot] += 1000

    if num_items(Items.Pumpkin) < reqs[Items.Pumpkin]:
        clear_unwanted(Entities.Pumpkin, Grounds.Soil)
        while num_items(Items.Pumpkin) < reqs[Items.Pumpkin]:
            if num_items(Items.Carrot) < 10:
                break
            pumpkins()
    else:
        reqs[Items.Pumpkin] += 1000

    if num_items(Items.Gold) < reqs[Items.Gold]:
        while num_items(Items.Gold) < reqs[Items.Gold]:
            if num_items(Items.Pumpkin) < 500:
                # need pumpkins for fertilizer
                break
            plant_maze()
            left_wall_solve()
    else:
        reqs[Items.Gold] += 1000

    if num_items(Items.Power) < reqs[Items.Power]:
        clear_unwanted(Entities.Sunflower, Grounds.Soil)
        while num_items(Items.Power) < reqs[Items.Power]:
            sunflowers()
    else:
        reqs[Items.Power] += 1000
