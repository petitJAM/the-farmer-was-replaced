
from cactus import cacti_sort
from fertilizing import fertilize
from maze_astar import maze_astar
from move_util import conv_xy, goto, world_range
from set_ground import reset_ground_to
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
        quick_print(queue)
        next = queue.pop(0)
        goto(next)
        if get_entity_type() != Entities.Pumpkin:
            if not plant(Entities.Pumpkin):
                return False
            water()
            queue.append(next)
        elif not can_harvest():
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

def cactus():
    cacti_sort()

items = "items"
func = "func"
seed = "seed"
ground = "ground"
required_amt = "required_amt"
require_inc = "require_inc"

world_size = get_world_size()**2

ALL_ITEMS = [
    Items.Carrot,
    Items.Carrot_Seed,
    Items.Empty_Tank,
    Items.Fertilizer,
    Items.Gold,
    Items.Hay,
    Items.Power,
    Items.Pumpkin,
    Items.Pumpkin_Seed,
    Items.Sunflower_Seed,
    Items.Water_Tank,
    Items.Wood,
    Items.Cactus,
    Items.Cactus_Seed,
    Items.Egg,
    Items.Bones,
]

# This min code might only exist because I didn't disable 
#  debug_item and though it wasn't working.
mins = {
    Items.Hay: 1,
    Items.Wood: 1,
    Items.Carrot: 1,
    Items.Pumpkin: 1,
    Items.Gold: 1,
    Items.Power: 1,
    Items.Cactus: 1,
}
for item in ALL_ITEMS:
    costs = get_cost(item)
    if costs != None:
        for c in costs:
            if c not in mins:
                mins[c] = 0
            mins[c] += costs[c]

quick_print(mins)
hay_min = mins[Items.Hay] * world_size * 2
wood_min = mins[Items.Wood] * world_size * 2
carrot_min = mins[Items.Carrot] * world_size * 2
pumpkin_min = mins[Items.Pumpkin] * world_size * 2
gold_min = mins[Items.Gold] * world_size * 2
power_min = mins[Items.Power] * world_size * 2
cacti_min = mins[Items.Cactus] * world_size * 2

controller = {
    items: [
        Items.Hay,
        Items.Wood,
        Items.Carrot,
        Items.Pumpkin,
        Items.Gold,
        Items.Power,
        Items.Cactus,
    ],

    Items.Hay: {
        func: hay,
        seed: None,
        ground: Grounds.Turf,
        required_amt: hay_min,
        require_inc: 1000,
    },
    Items.Wood: {
        func: wood,
        seed: None,
        ground: Grounds.Turf,
        required_amt: wood_min,
        require_inc: 1000,
    },
    Items.Carrot: {
        func: carrot,
        seed: Items.Carrot_Seed,
        ground: Grounds.Soil,
        required_amt: carrot_min,
        require_inc: 1000,
    },
    Items.Pumpkin: {
        func: pumpkin,
        seed: Items.Pumpkin_Seed,
        ground: Grounds.Soil,
        required_amt: pumpkin_min,
        require_inc: 1000,
    },
    Items.Gold: {
        func: maze_astar,
        seed: None,
        ground: Grounds.Turf,
        required_amt: gold_min,
        require_inc: 1000,
    },
    Items.Power: {
        func: power,
        seed: Items.Sunflower_Seed,
        ground: Grounds.Soil,
        required_amt: power_min,
        require_inc: 50,
    },
    Items.Cactus: {
        func: cactus,
        seed: Items.Cactus_Seed,
        ground: Grounds.Soil,
        required_amt: cacti_min,
        require_inc: 1000,
    }
}


debug_item = None
# debug_item = Items.Pumpkin

goto(0)

while True:
    world_size = get_world_size()**2

    reqs = list()
    reqs.append("h")
    reqs.append(controller[Items.Hay][required_amt])
    reqs.append("w")
    reqs.append(controller[Items.Wood][required_amt])
    reqs.append("c")
    reqs.append(controller[Items.Carrot][required_amt])
    reqs.append("p")
    reqs.append(controller[Items.Pumpkin][required_amt])
    reqs.append("g")
    reqs.append(controller[Items.Gold][required_amt])
    reqs.append("s")
    reqs.append(controller[Items.Power][required_amt])
    quick_print(reqs)


    for item in controller[items]:
        if debug_item != None and debug_item != item:
            continue

        control = controller[item]
        required_seed = control[seed]
        ground_check_required = True

        while num_items(item) < control[required_amt]:
            if required_seed != None and num_items(required_seed) < world_size*2:
                if not trade(required_seed, world_size*2):
                    quick_print("Can't trade for", required_seed)
                    break

            if ground_check_required:
                reset_ground_to(control[ground])

            goto(0)
            control[func]()

        # This occurs when we can't get enough seeds
        if num_items(item) >= control[required_amt]:
            control[required_amt] += control[require_inc]
