# pyright: reportOperatorIssue=false
from move_util import conv_idx, goto, world_range
from set_ground import reset_ground_to
from watering import water

def plant_cacti():
    for i in world_range():
        goto(i)
        if get_entity_type() != Entities.Cactus:
            plant(Entities.Cactus)
        water()


# Fancy-ish bubble sort
def sort_cacti():
    world_size = get_world_size()
    goto(0)

    n = 1
    sorted_idx_set = set()

    swapped = False

    while True:
        for i in world_range():
            if i in sorted_idx_set:
                continue

            goto(i)
            x = get_pos_x()
            y = get_pos_y()
            this_cactus_size = measure()

            # Swap as much as possible at each location to reduce iterations
            east_cactus_size = measure(East)
            if x < world_size-1 and this_cactus_size > east_cactus_size:
                swap(East)
                swapped = True
                # Keep the variables up-to-date so we can same time on measure() calls
                this_cactus_size, east_cactus_size = east_cactus_size, this_cactus_size
            if x > 0 and this_cactus_size < measure(West):
                swap(West)
                swapped = True

            # Same as above, but in the North-South direction
            north_cactus_size = measure(North)
            if y < world_size-1 and this_cactus_size > north_cactus_size:
                swap(North)
                swapped = True
                this_cactus_size, north_cactus_size = north_cactus_size, this_cactus_size
            if y > 0 and this_cactus_size < measure(South):
                swap(South)
                swapped = True

        if not swapped:
            break
        else:
            swapped = False

            # Optimize bubble sort by ignoring an expanding top right corner of
            #  cacti we know must be sorted.
            x = world_size - n
            y = world_size - n
            for ix in range(x, world_size):
                sorted_idx_set.add(conv_idx(ix, y))
            for iy in range(y, world_size):
                sorted_idx_set.add(conv_idx(x, iy))
            n += 1


def cactus():
    plant_cacti()
    sort_cacti()
    harvest()


world_size = get_world_size()**2
if num_items(Items.Cactus_Seed) < world_size and not trade(Items.Cactus_Seed, world_size*2):
    print("Cactus trade failed")
    print(get_cost(Items.Cactus_Seed))
    do_a_flip()
    print(get_cost(Items.Cactus_Seed)[Items.Gold] * world_size*2) # pyright: ignore[reportOptionalSubscript]

else:
    goto(0)
    reset_ground_to(Grounds.Soil)
    cactus()
