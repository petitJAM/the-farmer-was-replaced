from move_util import goto
from treat_land import water_old, fertilize_old
from walk_and_do import walk_and_do, walk_and_do_with_xy
from ensure_items import ensure_item

def carrots():
    def do_carrots():
        if num_items(Items.Carrot_Seed) == 0:
            trade(Items.Carrot_Seed, 5)
        if can_harvest():
            harvest()
        water_old()
        if get_entity_type() != Entities.Carrots:
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Carrots)

    walk_and_do(do_carrots)


def grass():
    def do_grass():
        if can_harvest():
            harvest()
        if get_ground_type() != Grounds.Turf:
            till()

    walk_and_do(do_grass)


def wood():
    def do_wood(x, y):
        if can_harvest():
            harvest()
        if x % 2 == y % 2:
            if get_entity_type() != Entities.Tree:
                plant(Entities.Tree)
        else:
            if get_entity_type() != Entities.Bush:
                plant(Entities.Bush)
        water_old()

    walk_and_do_with_xy(do_wood)

def pumpkins():
    queue = list(range(get_world_size()**2))

    while len(queue) > 0:
        next = queue.pop(0)
        goto(next)
        if get_entity_type() != Entities.Pumpkin:
            if not ensure_item(Items.Pumpkin_Seed):
                # Cannot get enough seeds, escape
                return False

            plant(Entities.Pumpkin)
            water_old()
            queue.append(next)

        while get_entity_type() != None and not can_harvest():
            fertilize_old()

    goto(0)
    while not can_harvest():
        do_a_flip()
    harvest()

    return True
