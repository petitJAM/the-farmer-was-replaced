from move_util import goto, world_range


def dinosaurs():
    for i in world_range():
        goto(i)
        if not hatch_dino():
            return False
        if get_group_size() >= 4:
            harvest()
    return True

# Note that this does not measure an entire group, just adjacent matches
def get_group_size():
    here = measure()
    size = 1
    if measure(North) == here:
        size += 1
    if measure(South) == here:
        size += 1
    if measure(West) == here:
        size += 1
    if measure(East) == here:
        size += 1
    return size

def hatch_dino():
    if get_entity_type() != Entities.Dinosaur and not use_item(Items.Egg):
        trade(Items.Egg, get_world_size())
        return use_item(Items.Egg)
    else:
        return True

while dinosaurs():
    pass
