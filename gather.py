
from better_maze import gold
from crops import carrots, pumpkins
from fertilizing import fertilize
from move_util import conv_xy, goto, world_range
from set_ground import reset_ground_to
from sunflowers import sunflowers
from treat_land import fertilize_old
from watering import water

def hay():
    for i in world_range():
        goto(i)
        if can_harvest():
            harvest()

def wood():
    for i in world_range():
        goto(i)

        if can_harvest():
            harvest()

        water()

        x, y = conv_xy(i)
        if x % 2 == y % 2:
            if get_entity_type() != Entities.Tree:
                plant(Entities.Tree)
        else:
            if get_entity_type() != Entities.Bush:
                plant(Entities.Bush)

def carrot():
    for i in world_range():
        goto(i)

        if can_harvest():
            harvest()

        water()

        if get_entity_type() != Entities.Carrots:
            plant(Entities.Carrots)

def pumpkin():
    queue = list(world_range())

    while len(queue) > 0:
        next = queue.pop(0)
        goto(next)
        if get_entity_type() != Entities.Pumpkin:
            if not plant(Entities.Pumpkin):
                return False
            water()
            queue.append(next)

    while not can_harvest():
        pass
    harvest()

    return True

def power():
    petal_coords = dict()

    for i in world_range():
        goto(i)

        if get_entity_type() != Entities.Sunflower and not plant(Entities.Sunflower):
            return False

        petals = measure()

        if petals not in petal_coords:
            petal_coords[petals] = list()

        petal_coords[petals].append(i)

    req = controller[Items.Power][required_amt]
    while num_items(Items.Power) < req:
        l = list()
        for k in petal_coords:
            l.append(k)
        quick_print(l)
        p = max(petal_coords)
        i = petal_coords[p].pop()
        if len(petal_coords[p]) == 0:
            petal_coords.pop(p)
        goto(i)

        while not can_harvest():
            fertilize()
        harvest()

        if not plant(Entities.Sunflower):
            return False

        petals = measure()
        if petals not in petal_coords:
            petal_coords[petals] = list()
        petal_coords[petals].append(i)


items = "items"
func = "func"
seed = "seed"
ground = "ground"
required_amt = "required_amt"
require_inc = "require_inc"

controller = {
    items: [
        Items.Hay,
        Items.Wood,
        Items.Carrot,
        Items.Pumpkin,
        Items.Gold,
        Items.Power,
    ],

    Items.Hay: {
        func: hay,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000,
    },
    Items.Wood: {
        func: wood,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000,
    },
    Items.Carrot: {
        func: carrot,
        seed: Items.Carrot_Seed,
        ground: Grounds.Soil,
        required_amt: 1000,
        require_inc: 1000,
    },
    Items.Pumpkin: {
        func: pumpkin,
        seed: Items.Pumpkin_Seed,
        ground: Grounds.Soil,
        required_amt: 1000,
        require_inc: 1000,
    },
    Items.Gold: {
        func: gold,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000,
    },
    Items.Power: {
        func: power,
        seed: Items.Sunflower_Seed,
        ground: Grounds.Soil,
        required_amt: 500,
        require_inc: 50,
    },
}


debug_item = None
# debug_item = Items.Power


while True:
    world_size = get_world_size()**2

    for item in controller[items]:
        if debug_item != None and debug_item != item:
            continue

        control = controller[item]
        required_seed = control[seed]
        ground_check_required = True

        quick_print("Processing", item, "with", control)

        while num_items(item) < control[required_amt]:
            if required_seed != None and not trade(required_seed, world_size):
                break

            if ground_check_required:
                reset_ground_to(control[ground])

            goto(0)
            control[func]()

        control[required_amt] += control[require_inc]

