from fertilizing import fertilize
from move_util import goto, world_range

def plant_maze():
    if get_entity_type() == Entities.Hedge:
        return

    for i in world_range():
        goto(i)
        if get_entity_type() != Entities.Bush and can_harvest():
            harvest()
        if get_ground_type() != Grounds.Turf:
            till()
        plant(Entities.Bush)

    while get_entity_type() != Entities.Hedge:
        fertilize()

clear()
plant_maze()
print("it's a amazing!")
