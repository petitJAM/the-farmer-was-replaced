from fertilizing import fertilize
from move_util import goto

def plant_maze():
    goto(0)
    if get_entity_type() == Entities.Hedge:
        return

    if get_ground_type() != Grounds.Turf:
        till()
    plant(Entities.Bush)

    while get_entity_type() != Entities.Hedge:
        fertilize()

clear()
plant_maze()
print("it's a amazing!")
