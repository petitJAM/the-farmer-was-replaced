from move_util import goto, world_range

def reset_ground_to(ground_type):
    for i in world_range():
        goto(i)
        if can_harvest():
            harvest()
        if get_ground_type() != ground_type:
            till()

def clear_unwanted(desired_entity, desired_ground):
    for i in world_range():
        goto(i)
        if get_entity_type() != desired_entity:
            harvest()
        if get_ground_type() != desired_ground:
            till()

def ensure(desired_entity, desired_ground):
    if get_entity_type() != desired_entity:
        harvest()
    if get_ground_type() != desired_ground:
        till()
