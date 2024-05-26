from move_util import goto
from walk_and_do import walk_and_do
from treat_land import fertilize_old

def plant_maze():
    if get_entity_type() == Entities.Hedge:
        return
    
    def plant_bush():
        if get_entity_type() != Entities.Bush and can_harvest():
            harvest()
        if get_ground_type() != Grounds.Turf:
            till()
        plant(Entities.Bush)

    goto(0)
    walk_and_do(plant_bush)
    goto(0)

    while get_entity_type() != Entities.Hedge:
        fertilize_old()

clear()
plant_maze()
print("it's a amazing!")
