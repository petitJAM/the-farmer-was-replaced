
from better_maze import gold
from crops import carrots, grass, pumpkins, wood
from move_util import goto
from set_ground import reset_ground_to
from sunflowers import sunflowers

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
        func: grass,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000
    },
    Items.Wood: {
        func: wood,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000
    },
    Items.Carrot: {
        func: carrots,
        seed: Items.Carrot_Seed,
        ground: Grounds.Soil,
        required_amt: 1000,
        require_inc: 1000
    },
    Items.Pumpkin: {
        func: pumpkins,
        seed: Items.Pumpkin_Seed,
        ground: Grounds.Soil,
        required_amt: 1000,
        require_inc: 1000
    },
    Items.Gold: {
        func: gold,
        seed: None,
        ground: Grounds.Turf,
        required_amt: 1000,
        require_inc: 1000
    },
    Items.Power: {
        func: sunflowers,
        seed: Items.Sunflower_Seed,
        ground: Grounds.Soil,
        required_amt: 500,
        require_inc: 500
    },
}


def check_cost(seed):
    world_size = get_world_size()**2

    if seed != None and num_items(seed) < world_size:
        seed_cost = get_cost(seed)
        if seed_cost != None:
            for required_item in seed_cost:
                cost = seed_cost[required_item]
                # Check if we have enough to do the entire world
                if num_items(required_item) < cost * world_size:
                    return False

while True:
    world_size = get_world_size()**2

    for item in controller[items]:
        control = controller[item]
        required_seed = control[seed]
        ground_check_required = True

        quick_print("Processing", item, "with", control)

        while num_items(item) < control[required_amt]:
            #check_cost(required_seed)
            if required_seed != None and not trade(required_seed, world_size):
                break

            if ground_check_required:
                reset_ground_to(control[ground])

            goto(0)
            control[func]()

        control[required_amt] += control[require_inc]

