from move_util import goto, goto_xy, world_range
from set_ground import reset_ground_to
from watering import water

def plant_cacti():
    for i in world_range():
        goto(i)
        if get_entity_type() != Entities.Cactus:
            plant(Entities.Cactus)
        #water()


def sort_cacti():
    world_size = get_world_size()
    goto(0)

    set_execution_speed(5)

    for y in range(world_size):
        goto_xy(0, y)
        sorted = False
        while not sorted:
            this_cactus_size = measure()
            next_cactus_size = measure(East)
            if this_cactus_size > next_cactus_size: # pyright: ignore[reportOperatorIssue]
                swap(East)
                move(East)


def cactus():
    plant_cacti()
    sort_cacti()


world_size = get_world_size()**2
if num_items(Items.Cactus_Seed) < world_size and not trade(Items.Cactus_Seed, world_size*2):
    quick_print("Cactus trade failed")

else:
    goto(0)
    #reset_ground_to(Grounds.Soil)
    cactus()
