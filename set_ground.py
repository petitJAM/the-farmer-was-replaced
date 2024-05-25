from walk_and_do import walk_and_do

def reset_ground_to(ground_type):
    def set_ground(x, y):
        if can_harvest():
            harvest()
        if get_ground_type() != ground_type:
            till()
    walk_and_do(set_ground)

def clear_unwanted(desired_entity, desired_ground):
    def harvest_andor_till():
        if get_entity_type() != desired_entity:
            harvest()
        if get_ground_type() != desired_ground:
            till()
    walk_and_do(harvest_andor_till)

def ensure(desired_entity, desired_ground):
    if get_entity_type() != desired_entity:
        harvest()
    if get_ground_type() != desired_ground:
        till()
